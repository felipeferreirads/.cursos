import re, subprocess, sys, os, tempfile, glob

BASE = os.path.dirname(os.path.abspath(__file__))

def slugify(name, maxlen=90):
    name = name.strip()
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    name = re.sub(r'\s+', ' ', name)
    return name[:maxlen].strip()

def download_vtt(video_id, langs):
    tmpdir = tempfile.mkdtemp(prefix="yt_")
    out_tpl = os.path.join(tmpdir, "%(id)s.%(ext)s")
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--write-subs", "--write-auto-subs", "--sub-lang", langs,
        "--skip-download", "--sub-format", "vtt",
        "-o", out_tpl,
        f"https://www.youtube.com/watch?v={video_id}",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    for lang in langs.split(","):
        files = glob.glob(os.path.join(tmpdir, f"{video_id}*.{lang}*.vtt"))
        if files:
            with open(files[0], encoding="utf-8") as f:
                return f.read(), lang, None
    files = glob.glob(os.path.join(tmpdir, f"{video_id}*.vtt"))
    if files:
        with open(files[0], encoding="utf-8") as f:
            return f.read(), "unknown", None
    return None, None, r.stderr[-500:]

def vtt_to_text(vtt):
    lines = vtt.splitlines()
    out = []
    prev = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if "-->" in line:
            continue
        if re.match(r'^\d+$', line):
            continue
        line = re.sub(r'<[^>]+>', '', line)
        line = line.strip()
        if not line:
            continue
        if line == prev:
            continue
        out.append(line)
        prev = line
    dedup = []
    for line in out:
        if dedup and (line in dedup[-1] or dedup[-1] in line):
            if len(line) > len(dedup[-1]):
                dedup[-1] = line
            continue
        dedup.append(line)
    return "\n".join(dedup)

def process(video_id, filename, folder, langs):
    outpath = os.path.join(folder, filename)
    if os.path.exists(outpath):
        print(f"SKIP (exists): {filename}")
        return
    vtt, used_lang, err = download_vtt(video_id, langs)
    if vtt is None:
        print(f"FAIL {video_id}: {err}")
        return
    text = vtt_to_text(vtt)
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(f"# {filename}\nVideo ID: {video_id}\nLang: {used_lang}\nURL: https://www.youtube.com/watch?v={video_id}\n\n---\n\n")
        f.write(text)
    print(f"OK ({used_lang}): {filename} ({len(text)} chars)")

WILLSEY = [
("AkgwxYfLN7Y","Ep01 - Intro to Earth"),
("MuOnqt8O_MY","Ep02 - Intro to Plate Tectonics"),
("dD5VN-ItEng","Ep03 - Divergent Plate Boundaries"),
("euGWKdTvfJM","Ep04 - Convergent Plate Boundaries"),
("PFSYRI2luXA","Ep05 - Transform Plate Boundaries"),
("O-mr2ELdqXM","Ep06 - Hot Spots"),
("la95gyEbauc","Ep07 - Minerals Part One"),
("dJIkbQ04z9o","Ep08 - Minerals Part Two"),
("ln10QYyDyYc","Ep09 - Igneous Rocks Part One"),
("Bwzo4A3trRs","Ep10 - Igneous Rocks Part Two"),
("ElbjiADZgHE","Ep11 - Intro to Volcanoes"),
("7LJ2EXtfycM","Ep12 - Volcano Types"),
("8NLzNLg-WNY","Ep13 - Volcanic Hazards"),
("6H0QMjIe-UM","Ep14 - Weathering"),
("b67Q0C-9rxc","Ep15 - Sedimentary Rocks"),
("P3HaSKspPIE","Ep16 - Metamorphic Rocks"),
("XXkCYq3d9lk","Ep17 - Relative Dating Principles"),
("dJn8x50jZWc","Ep18 - Unconformities"),
("AEWlKtmZdNs","Ep19 - Geo-Logic Puzzles"),
("8veMBs8-UV8","Ep20 - Absolute Dating"),
("82E98xrLIiE","Ep21 - Fossils"),
("B6LeJIVMFYI","Ep22 - The Geologic Time Scale"),
("JM2DAD-v98c","Ep23 - Intro to Rock Deformation"),
("HSW79_h7GNU","Ep24 - Explaining Strike and Dip"),
("2zgc6cpSQ0E","Ep25 - Measuring Strike and Dip"),
("IA10k3I4TUI","Ep26 - Folds in Rocks"),
("kwrBTzcqFAM","Ep27 - Know Your Faults"),
("GyLSqxxjz7o","Ep28 - Earthquake Basics"),
("BrRlO355RTk","Ep29 - Earthquake Location and Size"),
("PyGt9r9CvCA","Ep30 - Earthquake Hazards"),
("4wWBie0JF-w","Ep31 - Beachballs Explained"),
("YBfrIB1WVPA","Ep32 - Mass Wasting Basics"),
("ZNbkFw1zS-w","Ep33 - Types of Mass Wasting Processes"),
("PjzSy6fMt08","Ep34 - Stream Basics"),
("HxpIznKw8VU","Ep35 - Stream Landforms"),
("Uo0ols9fEls","Ep36 - Groundwater Concepts"),
("YBTSB5KcFAE","Ep37 - Groundwater Issues and Caves"),
("bsWZZlLJoy8","Ep38 - How Deserts Form"),
("gUFKiX6UJD8","Ep39 - Desert Landforms"),
]

PROFDAVE = [
("qNiOXc6pSBQ","01 - Introduction to Geology"),
("DWC2lZHaq5c","02 - History of the Earth Part 1"),
("DkRs6pPJ2k4","03 - History of the Earth Part 2"),
("UIxtzG9E_80","04 - History of the Earth Part 3"),
("5qSarYOhD_4","05 - History of the Earth Part 4"),
("7DuVsDOKUJM","06 - Geologic Structures Part 1"),
("aodnQWXYkZ0","07 - Geologic Structures Part 2"),
("n-ab1YPBdj8","08 - Overview of Earths Layers"),
("Prey5z8WQiU","09 - Earthquakes and Seismology"),
("oTrnz4Yy5m8","10 - Development of Plate Tectonics"),
("WBGWCeWhOq0","11 - Wilson Cycle and Plate Boundaries"),
("1TM8mvq_rhU","12 - Layers of the Ocean"),
("sAHHK2A1D2w","13 - Composition of Oceanic Crust Part 1"),
("3sUs8nso3z0","14 - Composition of Oceanic Crust Part 2"),
("cjbzAJrC8-Y","15 - Composition of Rocks Mineral Crystallinity"),
("-SxxefniyfY","16 - Macroscopic Characteristics Part 1"),
("zS6Lro53c-Q","17 - Macroscopic Characteristics Part 2"),
("A11b6tORIcM","18 - 8 Classes of Minerals Part 1"),
("ugdXW98JKxo","19 - 8 Classes of Minerals Part 2"),
("ryNQBxmcOu8","20 - Types of Silicates Part 1"),
("XO3yJkXrE6g","21 - Types of Silicates Part 2"),
("k6MH4K35xiE","22 - Origin of Igneous Rocks"),
("TtvSyROolsk","23 - Classification of Igneous Rocks"),
("HwBVL4AT7Wc","24 - Characteristics of Sedimentary Rocks"),
("0aWJCAmXkPc","25 - Mineralogy of Sedimentary Rocks"),
("8SQzXyt5UYk","26 - Classification Sedimentary Rocks Part 1"),
("Qqdf_26NVW0","27 - Classification Sedimentary Rocks Part 2"),
("Tq1WK6VKnZo","28 - Classification Sedimentary Rocks Part 3"),
("0QTkumoJnuU","29 - Origin of Metamorphic Rocks"),
("D9vcioJOUCc","30 - Types of Metamorphism"),
("VByCLpj-I_s","31 - The Rock Cycle"),
("NqF1per99lE","32 - Physical Weathering Processes"),
("JzsmkVUEy0Q","33 - Chemical Weathering Processes"),
("Ea47Gat0Oec","34 - Weathering Environments Part 1 Fluvial"),
("vOH7y-jKVSY","35 - Weathering Environments Part 2 Aeolian"),
("p01hH7_5U4g","36 - Weathering Environments Part 3 Glacial"),
("F7k1f1TiQ5c","37 - Methods of Dating Earth Part 1 Relative"),
("GwgxCQL2FLc","38 - Methods of Dating Earth Part 2 Absolute"),
("sd8cVCtIRO4","39 - Volcanoes Formation Types Activity"),
]

ESSX = [
("ND8Pbwg0EyY","01 - The Science of Geology"),
("Afc-UrsmkxE","02 - Continental Drift"),
("z58vSr_VTvk","03 - Plate Tectonics"),
("uzLt4AkP3O0","04 - Atoms and Chemical Bonds"),
("EZMBoXQbA6k","05 - Minerals"),
("PVF9jeH2-8U","06 - Igneous Rocks"),
("AoXU2sSrK9Q","07 - Origins of Lava and Magma"),
("gX4CQ-d9V7Y","08 - Volcanoes"),
("NMmNOUQL0Xc","09 - Weathering and Erosion"),
("0VzbhTP0ujI","10 - Soil"),
("6XbXM5y1110","11 - Sedimentary Rocks"),
("MeAz8An80ro","12 - Metamorphic Rocks"),
("f5ExuqB6SJI","13 - Earthquakes and Earths Interior"),
("W2Dh7-qLdSc","14 - The Ocean Floor"),
("sPJJT6zxd0k","15 - Faults Folds and Joints"),
("u6i_k4jdLUg","16 - Mountains"),
("-HIjmOS0vBs","17 - Landslides and Mass Wasting"),
("E_BypVAw5Zc","18 - Rivers and Springs"),
("1eu55XyKBSM","19 - Groundwater"),
("6VkbOSKQP1A","20 - Glaciers and Ice Sheets"),
("_ZbMtpBoxmo","21 - Deserts"),
("_dOpehNbCRk","22 - Geologic Time"),
("RnOsK5ImES4","23 - Farewell"),
]

CRASHCOURSE = [
("YokkwzdZX2A","00 - Crash Course Geology Preview"),
("ypH6dR7YGfU","01 - Intro to Geology"),
("3JdpD3X2Md8","02 - How did Earth form"),
("bouvNyq8xCY","03 - Earths Crust and Mantle Explained"),
("rm46SdVfB4I","04 - Whats at the center of the earth"),
("jQvv7CskMuo","05 - How Do Minerals Form"),
("lT_QAkL6lj0","06 - The Rock Episode"),
("eKnl_Jp8jsg","07 - How Do Gems Form"),
("AF2eYuAKsao","08 - Where Do Diamonds Come From"),
("xDll-p5g2EQ","09 - How Water Shapes the Land"),
("krXXSCb_P9Y","10 - What is Plate Tectonics"),
("r8uQVRVNV14","11 - How Do Mountains Form"),
("mLQYGG3SjyQ","12 - The Deepest Point in the World"),
("BMZbbewOLvU","13 - Volcanoes Explained"),
("WNvAic8KLb0","14 - Earthquakes Explained"),
]

def main():
    f_willsey = os.path.join(BASE, "EN-Geology101-Willsey")
    f_dave = os.path.join(BASE, "EN-ProfessorDaveExplains")
    f_essx = os.path.join(BASE, "PT-EarthAndSpaceSciencesX")
    f_cc = os.path.join(BASE, "EN-CrashCourseGeology")

    for vid, title in WILLSEY:
        process(vid, slugify(title) + ".txt", f_willsey, "en")
    for vid, title in PROFDAVE:
        process(vid, slugify(title) + ".txt", f_dave, "en")
    for vid, title in ESSX:
        process(vid, slugify(title) + ".txt", f_essx, "pt-BR,pt,en")
    for vid, title in CRASHCOURSE:
        process(vid, slugify(title) + ".txt", f_cc, "en")

if __name__ == "__main__":
    main()
