"""Merge public rich lists into one de-duplicated CSV of known ultra-high-net-worth individuals.

Sources (all public / openly licensed; see README section in the output notes):
  - komed3/rtb-api (MIT): Forbes real-time billionaires, current list + profiles of people who dropped off
  - FilesUploader/Forbes-Billionaire-List: Forbes annual billionaire lists 1996-2025
  - FilesUploader/Hurun-GRL: Hurun Global Rich List 2014-2024
  - hurun.net ranking data: Hurun China Rich List 1999-2026, India Rich List, Global Rich List,
    Richest Self-Made Women, Global U40 Self-Made Billionaires, China U40 Rich List
  - harveydevereux/TimesRichList2020: Sunday Times Rich List 2020 (UK top 1,000)
  - Wikidata: living people with a recorded net worth (P2218) >= $30M

Usage: python3 scripts/build_uhnw_csv.py [out.csv]
Paths to the downloaded sources are set in SOURCES below.
"""
import csv
import glob
import html
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

import pycountry

RTB = "/home/user/komed3/rtb-api/api"
DS = "/home/user/datasets"
UHNW_MIN_USD_M = 30.0

# Approximate USD conversion for Wikidata values in other currencies (order-of-magnitude use only).
WD_UNIT_USD = {
    "Q4917": 1.0,      # US dollar
    "Q4916": 1.08,     # euro
    "Q25224": 1.27,    # pound sterling
    "Q39099": 0.14,    # renminbi
    "Q80524": 0.012,   # Indian rupee
    "Q8146": 0.0067,   # yen
    "Q1104069": 0.73,  # Canadian dollar
    "Q259502": 0.65,   # Australian dollar
    "Q25344": 1.13,    # Swiss franc
    "Q202040": 0.00073,  # won
    "Q41044": 0.011,   # ruble
    "Q122922": 0.093,  # Swedish krona
    "Q132643": 0.093,  # Norwegian krone
    "Q25417": 0.145,   # Danish krone
    "Q31015": 0.128,   # Hong Kong dollar
    "Q4730": 0.055,    # Mexican peso? (not used if absent)
}
GBP_USD_2020 = 1.28

COUNTRY_FIX = {
    "uk": "GB", "united kingdom": "GB", "england": "GB", "scotland": "GB", "wales": "GB",
    "russia": "RU", "south korea": "KR", "korea": "KR", "taiwan": "TW", "hong kong": "HK",
    "macau": "MO", "macao": "MO", "china": "CN", "mainland china": "CN", "czech republic": "CZ",
    "vietnam": "VN", "turkey": "TR", "iran": "IR", "venezuela": "VE", "tanzania": "TZ",
    "bolivia": "BO", "eswatini (swaziland)": "SZ", "swaziland": "SZ", "st. kitts and nevis": "KN",
    "st. kitts & nevis": "KN", "ivory coast": "CI", "the netherlands": "NL", "uae": "AE",
    "united arab emirates": "AE", "usa": "US", "us": "US", "united states": "US",
    "guernsey": "GG", "monaco": "MC", "liechtenstein": "LI", "kingdom of the netherlands": "NL",
    "people's republic of china": "CN", "republic of ireland": "IE", "russian federation": "RU",
    "laos": "LA", "moldova": "MD", "syria": "SY", "palestine": "PS", "kosovo": "XK",
}
_country_cache = {}


def iso2(value):
    if not value:
        return ""
    v = str(value).strip()
    if not v:
        return ""
    key = v.lower()
    if key in _country_cache:
        return _country_cache[key]
    code = ""
    if key in COUNTRY_FIX:
        code = COUNTRY_FIX[key]
    elif len(v) == 2 and v.isalpha():
        code = v.upper()
    else:
        first = re.split(r"[-,/]", v)[0].strip()  # "China-Fujian-Longyan" -> "China"
        for cand in (v, first):
            if cand.lower() in COUNTRY_FIX:
                code = COUNTRY_FIX[cand.lower()]
                break
            try:
                code = pycountry.countries.lookup(cand).alpha_2
                break
            except LookupError:
                continue
    _country_cache[key] = code
    return code


def country_name(code):
    if not code:
        return ""
    if code == "XK":
        return "Kosovo"
    c = pycountry.countries.get(alpha_2=code)
    return getattr(c, "common_name", None) or (c.name if c else code)


TITLES = r"^(sir|dame|lord|lady|dr|the hon|hon|baron|baroness|sheikh|shaikh|prince|princess|mr|mrs|ms)\.?\s+"


def norm_name(name):
    n = unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower()
    n = re.sub(r"\(.*?\)", " ", n)
    n = re.sub(r"(&|\band\b)\s*(his |her )?(family|siblings|sons|daughters|children)\b.*$", " ", n)
    n = re.sub(r"\bfamily\b", " ", n)
    n = re.sub(r"[^a-z0-9 ]", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    prev = None
    while prev != n:
        prev = n
        n = re.sub(TITLES, "", n)
    return n


def fnum(x):
    if x is None:
        return None
    s = re.sub(r"[^0-9.\-]", "", str(x))
    try:
        return float(s) if s not in ("", ".", "-") else None
    except ValueError:
        return None


records = []  # dicts: name, nw_usd_m, as_of, country, wealth_source, industry, list, year, uri, wikidata, deceased


CURRENT_SRC = ""


FAMILY_SUFFIX = re.compile(r"\s*(,\s*)?(\(|&|\band\b)\s*(his |her )?(family|siblings|sons|daughters|children)\)?\s*$", re.I)


def split_joint(name):
    """'David and Simon Reuben' -> ['David Reuben', 'Simon Reuben']; 'Liu Zaiwang & Fu Haixia' -> both;
    'Schwab, Charles R.' -> ['Charles R. Schwab']."""
    n = html.unescape(name or "").strip()
    n = FAMILY_SUFFIX.sub("", n).strip(" ,")
    if "," in n and not re.search(r"、|&|\band\b", n) and n.count(",") == 1:
        last, first = [x.strip() for x in n.split(",")]
        if first.lower().rstrip(".") in ("jr", "sr", "ii", "iii"):
            return [n]
        return [f"{first} {last}".strip()]
    parts = [x.strip(" ,") for x in re.split(r"\s*[、·]\s*|\s+&\s+|\s+and\s+|\s*;\s*", n) if x.strip(" ,")]
    if len(parts) <= 1:
        return [n]
    last_toks = parts[-1].split()
    if len(last_toks) >= 2:
        surname = last_toks[-1]
        return [p + " " + surname if len(p.split()) == 1 else p for p in parts[:-1]] + [parts[-1]]
    return parts


def add(**kw):
    kw.setdefault("src", CURRENT_SRC)
    names = split_joint(kw.get("name", ""))
    if len(names) > 1 and not kw.get("_split"):
        for nm in names:
            others = [o for o in names if o != nm]
            add(**{**kw, "name": nm, "_split": True, "joint_with": kw.get("joint_with") or ", ".join(others)})
        return
    if names:
        kw["name"] = names[0]
    if not (kw.get("name") or "").strip():
        return
    kw["name"] = re.sub(r"\s+", " ", kw["name"]).strip()
    kw["country"] = iso2(kw.get("country"))
    records.append(kw)


# 1. Forbes real-time current list
CURRENT_SRC = "rtb-current"
cur_files = sorted(glob.glob(f"{RTB}/list/rtb/20*"))
cur = json.load(open(cur_files[-1], encoding="utf-8"))
current_uris = set()
for r in cur["list"]:
    current_uris.add(r["uri"])
    add(name=r["name"], nw_usd_m=r.get("networth"), as_of=cur["date"], country=r.get("citizenship"),
        wealth_source="; ".join(r.get("source", [])), industry="; ".join(r.get("industry", [])),
        list="Forbes real-time", year=int(cur["date"][:4]), uri=r["uri"])

# 2. Forbes real-time profiles of people no longer on the list
deceased_uris = set(json.load(open(f"{RTB}/filter/deceased", encoding="utf-8"))) if os.path.exists(f"{RTB}/filter/deceased") else set()
CURRENT_SRC = "rtb-profiles"
for d in glob.glob(f"{RTB}/profile/*/"):
    uri = os.path.basename(d.rstrip("/"))
    if uri in current_uris or not os.path.exists(d + "info"):
        continue
    try:
        info = json.load(open(d + "info", encoding="utf-8"))
        latest = json.load(open(d + "latest", encoding="utf-8")) if os.path.exists(d + "latest") else {}
    except (json.JSONDecodeError, OSError):
        continue  # incomplete download
    dead = bool(info.get("deceased")) or uri in deceased_uris
    add(name=info.get("name", ""), nw_usd_m=latest.get("networth"), as_of=latest.get("date", ""),
        country=info.get("citizenship"), wealth_source="; ".join(info.get("source", []) or []),
        industry="; ".join(info.get("industry", []) or []), list="Forbes real-time (former)",
        year=int(latest["date"][:4]) if latest.get("date") else None, uri=uri, deceased=dead)

# 3. Forbes annual lists 1996-2025
for f in glob.glob(f"{DS}/FilesUploader_Forbes-Billionaire-List/*.csv"):
    CURRENT_SRC = f
    year = int(re.search(r"(\d{4})", os.path.basename(f)).group(1))
    for r in csv.DictReader(open(f, encoding="utf-8-sig", errors="replace")):
        w = fnum(r.get("Wealth (in $1B USD)"))
        add(name=r.get("Name", ""), nw_usd_m=w * 1000 if w is not None else None, as_of=str(year),
            country=r.get("Country of Citizenship"), wealth_source=r.get("Source of Wealth", ""),
            industry=r.get("Industry", ""), list="Forbes annual", year=year)

# 4. Hurun Global Rich List CSVs 2014-2024
for f in glob.glob(f"{DS}/FilesUploader_Hurun-GRL/*.csv"):
    CURRENT_SRC = f
    year = int(re.search(r"(\d{4})", os.path.basename(f)).group(1))
    for r in csv.DictReader(open(f, encoding="utf-8-sig", errors="replace")):
        w = fnum(r.get("Wealth (in $1B USD)"))
        add(name=r.get("Name", ""), nw_usd_m=w * 1000 if w is not None else None, as_of=str(year),
            country=r.get("Country Headquartered"), wealth_source=r.get("Company", ""),
            industry=r.get("Industry", ""), list="Hurun Global", year=year)

# 5. hurun.net downloads (China, India, Global, women, U40 lists)
HURUN_LABEL = {"china": "Hurun China", "india": "Hurun India", "global": "Hurun Global",
               "cwomen": "Hurun Self-Made Women", "gu40": "Hurun Global U40", "u40": "Hurun China U40"}
def hv(r, suffix):
    """Value of hs_Rank_<List>_<suffix>; each Hurun list uses its own <List> prefix (Rich, India, Global, ...)."""
    for k, v in r.items():
        if re.fullmatch(r"hs_Rank_[A-Za-z0-9]+_" + suffix, k) and v not in (None, ""):
            return v
    return None


INR_CRORE_USD_M = 0.12  # 1 crore INR ~ $0.12M (approximate)
for sub, label in HURUN_LABEL.items():
    for f in glob.glob(f"{DS}/hurun/{sub}/*.json"):
        CURRENT_SRC = f
        d = json.load(open(f, encoding="utf-8"))
        label_year = re.search(r"(\d{4})", d["label"])
        for r in d["rows"]:
            year = fnum(hv(r, "Year"))
            year = int(year) if year else (int(label_year.group(1)) if label_year else None)
            chars = [c for c in (r.get("hs_Character") or []) if (c.get("hs_Character_Fullname_En") or c.get("hs_Character_Fullname_Cn"))]
            usd = fnum(hv(r, "Wealth_USD"))
            if usd is not None and sub in ("global", "gu40", "cwomen") and usd < 1000:
                usd *= 1000  # these billionaire lists give USD in billions, not millions
            if usd is None and fnum(hv(r, "Wealth_INR")) is not None:
                usd = fnum(hv(r, "Wealth_INR")) * INR_CRORE_USD_M
            default_country = hv(r, "Permanent_En") or ("China" if sub in ("china", "u40") else "India" if sub == "india" else "")
            common = dict(nw_usd_m=usd, as_of=str(year or ""), list=label, year=year,
                          wealth_source=hv(r, "ComName_En") or hv(r, "ComName_Cn") or "",
                          industry=hv(r, "Industry_En") or "")
            if not chars:  # no per-person records: fall back to the entry name
                add(name=hv(r, "ChaName_En") or hv(r, "ChaName_Cn") or "",
                    country=default_country, name_cn=hv(r, "ChaName_Cn") or "", **common)
                continue
            # one record per person; joint entries (couples, families) share the listed wealth
            names = [c.get("hs_Character_Fullname_En") or c.get("hs_Character_Fullname_Cn") for c in chars]
            for c, nm in zip(chars, names):
                others = [o for o in names if o != nm]
                add(name=nm, country=c.get("hs_Character_Permanent_En") or default_country,
                    name_cn=c.get("hs_Character_Fullname_Cn") or "",
                    joint_with=", ".join(others), **common)

# 5b. Hurun Global Unicorn Index: founders of private companies valued at $1B+. Their personal net worth is not
# published; they are included as likely UHNW (basis = unicorn founder) with no net-worth figure.
for f in sorted(glob.glob(f"{DS}/hurun/unicorn/*.json")):
    CURRENT_SRC = f
    d = json.load(open(f, encoding="utf-8"))
    for r in d["rows"]:
        year = fnum(hv(r, "Year"))
        names = re.split(r"\s*[,、;/]\s*|\s+&\s+|\s+and\s+", hv(r, "ChaName_En") or "")
        val = fnum(hv(r, "Wealth_USD"))
        company = hv(r, "ComName_En") or hv(r, "ComName_Cn") or ""
        hq = (hv(r, "ComHeadquarters_En") or "").split("-")[0]
        for nm in names:
            if len(nm.split()) < 2 and not re.search(r"[一-鿿]", nm):
                continue  # skip single tokens / placeholders
            add(name=nm, nw_usd_m=None, as_of=str(int(year)) if year else "", country="",  # HQ != founder's country
                wealth_source=f"{company} (founder; company valued ${val:,.0f}B)" if val else f"{company} (founder)",
                industry=hv(r, "Industry_En") or "", list="Hurun Unicorn founders", year=int(year) if year else None)

# 6. Sunday Times Rich List 2020
CURRENT_SRC = "sunday-times-2020"
f = f"{DS}/harveydevereux_TimesRichList2020/resources/TimesRichList2020.csv"
if os.path.exists(f):
    for r in csv.DictReader(open(f, encoding="utf-8-sig", errors="replace")):
        w = fnum(r.get("Worth"))
        add(name=r.get("Name", ""), nw_usd_m=w * GBP_USD_2020 / 1e6 if w else None, as_of="2020",
            country="GB", wealth_source=r.get("Source of wealth", ""), industry="",
            list="Sunday Times Rich List", year=2020)

# 7. Wikidata (living people with a net worth statement)
CURRENT_SRC = "wikidata"
wd_best = {}
for r in csv.DictReader(open(f"{DS}/wikidata/wd_networth.csv", encoding="utf-8")):
    unit = r["unit"].rsplit("/", 1)[-1]
    rate = WD_UNIT_USD.get(unit)
    amt = fnum(r["nw"])
    if rate is None or amt is None:
        continue
    usd_m = amt * rate / 1e6
    date = (r.get("date") or "")[:10]
    if not re.match(r"\d{4}", date):
        date = ""  # unknown or blank-node date
    key = r["p"]
    if key not in wd_best or date > wd_best[key]["as_of"]:
        wd_best[key] = dict(name=r["pLabel"], nw_usd_m=usd_m, as_of=date, country=r.get("country"),
                            wealth_source="", industry="", list="Wikidata",
                            year=int(date[:4]) if date else None, wikidata=key)
for v in wd_best.values():
    if v["nw_usd_m"] >= UHNW_MIN_USD_M and not re.fullmatch(r"Q\d+", v["name"]):
        add(**v)

# 8. SEC insider holdings (scripts/sec_insiders.py). Names are matched to people already on a rich list by
# surname + first initial + (company-word overlap or same first 3 letters of first name). Unmatched people whose
# SEC estimate exceeds $1B are dropped: Forbes/Hurun track essentially every public-stock billionaire, so such
# rows are price/unit errors (foreign-currency or ADR mismatches) or name variants of someone already listed.
SEC_FILE = "data/sec_insiders_30m.csv"
GENERIC = {"inc", "corp", "corporation", "co", "company", "holdings", "holding", "group", "the", "ltd", "plc", "sa",
           "nv", "llc", "lp", "de", "technologies", "technology", "international", "and", "of", "com", "class",
           "partners", "trust", "financial", "bancorp", "industries", "systems", "global", "brands", "energy"}


def words(s):
    return {w for w in re.sub(r"[^a-z0-9 ]", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).split()
            if len(w) > 2 and w not in GENERIC}


sec_stats = Counter()
CURRENT_SRC = "sec"
if os.path.exists(SEC_FILE):
    idx = defaultdict(list)  # (surname, first initial) -> [(first token, name, wealth words)]
    for r in records:
        toks = norm_name(r["name"]).split()
        if len(toks) >= 2:
            idx[(toks[-1], toks[0][0])].append((toks[0], r["name"], words(r.get("wealth_source", ""))))
            idx[(toks[0], toks[-1][0])].append((toks[-1], r["name"], words(r.get("wealth_source", ""))))  # surname-first (e.g. Chinese) names
    sec_rows = list(csv.DictReader(open(SEC_FILE, encoding="utf-8")))
    pending, unmatched_big_by_issuer = [], Counter()
    for s in sec_rows:
        st = norm_name(s["sec_name"]).split()  # SEC order: LAST FIRST MIDDLE
        if len(st) < 2:
            continue
        surname, first = st[0], st[1]
        cw = words(re.sub(r"\(.*?\)|-.*?(;|$)", " ", s["companies"]))
        match = None
        for ftok, nm, ww in idx.get((surname, first[0]), []):
            if (cw & ww) or ftok[:3] == first[:3]:
                match = nm
                break
        val = float(s["est_public_holdings_usd_m"])
        if match is None and val > 1000:
            for ik in s["issuer_ciks"].split(";"):
                unmatched_big_by_issuer[ik] += 1
            sec_stats["dropped: unmatched SEC estimate > $1B"] += 1
            continue
        pending.append((s, match, val))
    bad_issuers = {ik for ik, n in unmatched_big_by_issuer.items() if n >= 2}
    for s, match, val in pending:
        iks = set(s["issuer_ciks"].split(";"))
        if match is None and iks and iks <= bad_issuers:
            sec_stats["dropped: company with implausible insider values"] += 1
            continue
        sec_stats["matched to rich list" if match else "added (SEC only)"] += 1
        add(name=match or s["name"], nw_usd_m=val, as_of=s["as_of"], country="" if not match else None,
            wealth_source=s["companies"], industry="", list="SEC insider holdings", year=int(s["as_of"][:4]),
            sec_cik=s["owner_cik"])
    print("SEC:", dict(sec_stats))

wd_dead_names = set()
dead_file =f"{DS}/wikidata/wd_dead.csv"
if os.path.exists(dead_file):
    wd_dead_names = {norm_name(r["pLabel"]) for r in csv.DictReader(open(dead_file, encoding="utf-8"))}
# Exact-name matches against Wikidata businesspeople with a death date (checked for names not listed since 2024)
dead_file2 = f"{DS}/wikidata/wd_dead_by_name.csv"
if os.path.exists(dead_file2):
    wd_dead_names |= {norm_name(r["name"]) for r in csv.DictReader(open(dead_file2, encoding="utf-8"))}
RECENT_YEAR = 2025
dropped = Counter()

# ---- merge: group by normalised name, split by country where they clearly differ ----
by_name = defaultdict(list)
for r in records:
    k = norm_name(r["name"])
    if k:
        by_name[k].append(r)

people = []
for k, rs in by_name.items():
    countries = Counter(r["country"] for r in rs if r["country"])
    # Split only when a single list names this person more than once in the same year with different
    # countries, i.e. the source itself says these are different people (e.g. several "Wang Wei"s).
    by_key = defaultdict(set)
    for r in rs:
        if r["country"]:
            by_key[(r["src"], r.get("year"))].add(r["country"])
    dup_countries = set().union(*[c for c in by_key.values() if len(c) > 1]) if by_key else set()
    if len(dup_countries) < 2:
        groups = [rs]
    else:
        main = max(dup_countries, key=lambda c: countries[c])
        groups_d = defaultdict(list)
        for r in rs:
            groups_d[r["country"] if r["country"] in dup_countries else main].append(r)
        groups = list(groups_d.values())
    people.extend(groups)

# ---- second pass: merge name variants of the same person ----
# e.g. "Jen Hsun Huang" / "Jensen Huang", "Lawrence Ellison" / "Larry Ellison", "Yiming Zhang" / "Zhang Yiming".
# Two groups merge when they share a surname, their first names are equivalent (nickname, prefix, or initial for
# SEC-style names) AND they share a company word; or when their name tokens are the same set in a different order
# AND they share a company word or country.
NICK = {}
for canon, alts in {
    "william": "bill billy will willy", "robert": "bob bobby rob robbie bert", "richard": "dick rick ricky rich",
    "james": "jim jimmy jamie", "john": "jack johnny jon", "jonathan": "jon jonny", "michael": "mike mick mikey",
    "thomas": "tom tommy", "charles": "chuck charlie chas", "lawrence": "larry laurence", "jeffrey": "jeff geoffrey",
    "stephen": "steve steven stevie", "daniel": "dan danny", "david": "dave davey", "kenneth": "ken kenny",
    "anthony": "tony", "edward": "ed eddie ted ned", "joseph": "joe joey", "samuel": "sam sammy", "benjamin": "ben benny",
    "andrew": "andy drew", "christopher": "chris kit", "patrick": "pat paddy", "ronald": "ron ronnie",
    "donald": "don donnie", "nicholas": "nick nicky", "matthew": "matt", "alexander": "alex sasha alec",
    "gregory": "greg", "peter": "pete", "henry": "hank harry", "frederick": "fred freddie", "gerald": "gerry jerry",
    "timothy": "tim timmy", "philip": "phil", "phillip": "phil", "leonard": "len lenny leo", "theodore": "ted teddy theo",
    "elizabeth": "liz beth betsy betty eliza lisa", "katherine": "kate kathy katie catherine kathryn",
    "margaret": "maggie meg peggy", "jennifer": "jen jenny", "susan": "sue susie", "deborah": "deb debbie",
    "patricia": "pat patty trish", "rebecca": "becky", "victoria": "vicky tori", "abigail": "abby", "jensen": "jen",
}.items():
    for a in alts.split() + [canon]:
        NICK.setdefault(a, canon)


def first_equiv(a, b):
    if a == b or NICK.get(a, a) == NICK.get(b, b):
        return True
    return False


def gkey(g):
    nm = norm_name(min(g, key=lambda r: LIST_PRIORITY_PRE.get(r["list"], 9))["name"])
    return nm.split()


LIST_PRIORITY_PRE = {"Forbes real-time": 0, "Forbes real-time (former)": 1, "Forbes annual": 2}
ginfo = []
for g in people:
    toks = gkey(g)
    ww = set()
    for r in g:
        ww |= words(r.get("wealth_source", ""))
    ginfo.append((toks, ww, {r["country"] for r in g if r["country"]}, {(r["src"], r.get("year")) for r in g}))

parent = list(range(len(people)))


def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i


blocks = defaultdict(list)
SUFFIXES = {"jr", "sr", "ii", "iii", "iv", "v"}
for i, (toks, ww, cs, srcs) in enumerate(ginfo):
    core = [t for t in toks if t not in SUFFIXES]
    if len(core) >= 2:
        blocks[("s", core[-1])].append(i)                 # surname last (Western order)
        blocks[("s", core[0])].append(i)                  # surname first (Chinese / SEC order)
merged_pairs = 0
for key, idxs in blocks.items():
    if len(idxs) < 2 or len(idxs) > 400:
        continue
    for a_i in range(len(idxs)):
        for b_i in range(a_i + 1, len(idxs)):
            a, b = idxs[a_i], idxs[b_i]
            if find(a) == find(b):
                continue
            ta, wa, ca, sa = ginfo[a]
            tb, wb, cb, sb = ginfo[b]
            if sa & sb:
                continue  # the same list names both in the same year -> different people (e.g. father/son)
            if {t for t in ta if t in SUFFIXES} != {t for t in tb if t in SUFFIXES}:
                continue  # III vs IV, Jr vs none
            shared_company = bool(wa & wb)
            if sorted(ta) == sorted(tb):
                ok = shared_company or bool(ca & cb)
            else:
                # surname = the block key; compare the given names on each side
                sur = key[1]
                fa = [t for t in ta if t != sur and len(t) > 1 and t not in ("and", "jr", "sr", "ii", "iii")]
                fb = [t for t in tb if t != sur and len(t) > 1 and t not in ("and", "jr", "sr", "ii", "iii")]
                ok = bool(fa and fb) and shared_company and first_equiv(fa[0], fb[0])
            if ok:
                parent[find(a)] = find(b)
                merged_pairs += 1
MERGE_LOG = []
merged = defaultdict(list)
for i, g in enumerate(people):
    merged[find(i)].extend(g)
import random
random.seed(1)
_names = defaultdict(set)
for i, g in enumerate(people):
    _names[find(i)].add(min(g, key=lambda r: LIST_PRIORITY_PRE.get(r["list"], 9))["name"])
_multi = [sorted(v) for v in _names.values() if len(v) > 1]
with open("/tmp/claude-0/-home-user-anna/11e881aa-a635-56c4-ac1a-08b9de9b2955/scratchpad/merge_sample.txt", "w") as fh:
    for v in random.sample(_multi, min(60, len(_multi))):
        fh.write(" | ".join(v) + "\n")
print(f"name-variant merges: {merged_pairs} ({len(people)} -> {len(merged)} groups)")
people = list(merged.values())

LIST_PRIORITY = {"Forbes real-time": 0, "Forbes real-time (former)": 1, "Forbes annual": 2, "Hurun Global": 3,
                 "Hurun China": 3, "Hurun India": 3, "Hurun Self-Made Women": 4, "Hurun Global U40": 4,
                 "Hurun China U40": 4, "Sunday Times Rich List": 5, "Wikidata": 6,
                 "SEC insider holdings": 7, "Hurun Unicorn founders": 8}


def as_of_key(r):
    a = str(r.get("as_of") or "")
    return (a + "-06-30") if len(a) == 4 else a  # year-only lists: mid-year, so a dated real-time figure from later that year wins


out_rows = []
for g in people:
    g_sorted = sorted(g, key=lambda r: (as_of_key(r), -LIST_PRIORITY.get(r["list"], 9)), reverse=True)
    # rich-list estimates beat the SEC figure (which only counts public stock in companies where they are insiders)
    best = next((r for r in g_sorted if r.get("nw_usd_m") is not None and r["list"] != "SEC insider holdings"), None) \
        or next((r for r in g_sorted if r.get("nw_usd_m") is not None), g_sorted[0])
    display = min(g, key=lambda r: LIST_PRIORITY.get(r["list"], 9))["name"]
    lists = defaultdict(set)
    for r in g:
        if r.get("year"):
            lists[r["list"]].add(r["year"])
        else:
            lists[r["list"]]
    appears = []
    for name_, yrs in sorted(lists.items(), key=lambda kv: LIST_PRIORITY.get(kv[0], 9)):
        if yrs:
            appears.append(f"{name_} ({min(yrs)}-{max(yrs)})" if min(yrs) != max(yrs) else f"{name_} ({min(yrs)})")
        else:
            appears.append(name_)
    years = [r["year"] for r in g if r.get("year")]
    deceased = any(r.get("deceased") for r in g)
    uri = next((r["uri"] for r in g if r.get("uri")), "")
    wd = next((r["wikidata"] for r in g if r.get("wikidata")), "")
    sec_cik = next((r["sec_cik"] for r in g if r.get("sec_cik")), "")
    sec_companies = next((r["wealth_source"] for r in g if r.get("sec_cik")), "")
    country = best["country"] or next((r["country"] for r in g if r["country"]), "")
    ws = best.get("wealth_source") or next((r["wealth_source"] for r in g_sorted if r.get("wealth_source")), "")
    ind = best.get("industry") or next((r["industry"] for r in g_sorted if r.get("industry")), "")
    name_cn = next((r["name_cn"] for r in g if r.get("name_cn")), "")
    joint = best.get("joint_with") or ""
    nw = best.get("nw_usd_m")
    last_year = max(years) if years else 0
    if deceased:
        dropped["deceased (Forbes)"] += 1
        continue
    if norm_name(display) in wd_dead_names and last_year < RECENT_YEAR:
        dropped["deceased (Wikidata, not listed since 2024)"] += 1
        continue
    if nw is not None and nw < UHNW_MIN_USD_M:
        dropped["last known net worth under $30M"] += 1
        continue
    out_rows.append({
        "name": display,
        "name_chinese": name_cn,
        "latest_net_worth_usd_m": round(nw, 1) if nw is not None else "",
        "net_worth_as_of": best.get("as_of", ""),
        "net_worth_source": best["list"],
        "net_worth_shared_with": joint,
        "country": country_name(country),
        "country_code": country,
        "source_of_wealth": ws,
        "industry": ind,
        "appears_on": "; ".join(appears),
        "first_listed_year": min(years) if years else "",
        "last_listed_year": max(years) if years else "",
        "possibly_deceased": "yes" if norm_name(display) in wd_dead_names else "",  # still on a recent list
        "forbes_profile_url": f"https://www.forbes.com/profile/{uri}/" if uri else "",
        "wikidata_url": wd,
        "sec_insider_companies": sec_companies,
        "sec_filings_url": f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={sec_cik}&type=4" if sec_cik else "",
    })

out_rows.sort(key=lambda r: -(r["latest_net_worth_usd_m"] or 0))
out = sys.argv[1] if len(sys.argv) > 1 else "data/uhnw_individuals.csv"
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
    w.writeheader()
    w.writerows(out_rows)

print(f"input records: {len(records)}")
print("records by list:", dict(Counter(r["list"] for r in records)))
print("dropped:", dict(dropped))
print(f"unique living individuals written: {len(out_rows)} -> {out}")
