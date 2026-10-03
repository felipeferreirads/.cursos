import re, subprocess, sys, os, tempfile, glob, unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))

def slugify(name, maxlen=70):
    name = name.strip()
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    name = re.sub(r'\s+', ' ', name)
    return name[:maxlen].strip()

def download_vtt(video_id):
    tmpdir = tempfile.mkdtemp(prefix="yt_")
    out_tpl = os.path.join(tmpdir, "%(id)s.%(ext)s")
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--write-auto-subs", "--sub-lang", "pt",
        "--skip-download", "--sub-format", "vtt",
        "-o", out_tpl,
        f"https://www.youtube.com/watch?v={video_id}",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    files = glob.glob(os.path.join(tmpdir, f"{video_id}*.vtt"))
    if not files:
        return None, r.stderr[-500:]
    with open(files[0], encoding="utf-8") as f:
        return f.read(), None

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
        # strip inline timestamp tags like <00:00:01.130><c> word</c>
        line = re.sub(r'<[^>]+>', '', line)
        line = line.strip()
        if not line:
            continue
        if line == prev:
            continue
        out.append(line)
        prev = line
    # collapse further: remove lines that are pure substrings/duplicates of the immediately previous accumulated text due to rolling captions
    dedup = []
    for line in out:
        if dedup and (line in dedup[-1] or dedup[-1] in line):
            if len(line) > len(dedup[-1]):
                dedup[-1] = line
            continue
        dedup.append(line)
    return "\n".join(dedup)

def process(video_id, filename, folder):
    outpath = os.path.join(folder, filename)
    if os.path.exists(outpath):
        print(f"SKIP (exists): {filename}")
        return
    vtt, err = download_vtt(video_id)
    if vtt is None:
        print(f"FAIL {video_id}: {err}")
        return
    text = vtt_to_text(vtt)
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(f"# {filename}\nVideo ID: {video_id}\nURL: https://www.youtube.com/watch?v={video_id}\n\n---\n\n")
        f.write(text)
    print(f"OK: {filename} ({len(text)} chars)")

PLAYLIST_NUMERADA = [
    ("vMvPq5Wps1M","01 - Cursos USP Sistema Terra"),
    ("Tc7bt_DLfCM","02 - Cursos USP Sistema Terra"),
    ("L2hMr_EBUtM","03 - Cursos USP Sistema Terra"),
    ("qHhGZWm27zU","04 - Cursos USP Sistema Terra"),
    ("ut5DUJhO-G8","05 - Cursos USP Sistema Terra"),
    ("4N6VhvGwIQ4","06 - Cursos USP Sistema Terra"),
    ("JpNO_LmeXIQ","07 - Cursos USP Sistema Terra"),
    ("L0kGaGbVg-c","08 - Cursos USP Sistema Terra"),
    ("cDle-Xg2wng","09 - Cursos USP Sistema Terra"),
    ("VhOtrJmZIUk","10 - Cursos USP Sistema Terra"),
    ("v4XDaZpmty0","11 - Cursos USP Sistema Terra"),
    ("aZNzn8Nn-Fs","12 - Cursos USP Sistema Terra"),
    ("2AJTdU1L4ho","13 - Cursos USP Sistema Terra"),
    ("ZIbA2h7L7V8","14 - Rochas Igneas (Aula 6 parte 1)"),
    ("3U8lUYJ7c68","15 - Cursos USP Sistema Terra"),
    ("ZHZh83BDDPQ","16 - Cursos USP Sistema Terra"),
    ("7jjz6kaWlzw","17 - Cursos USP Sistema Terra"),
    ("6gUCIdfN7Pw","18 - Cursos USP Sistema Terra"),
    ("X_y5AeFe_dI","19 - Cursos USP Sistema Terra"),
    ("hLGxQqf5EkM","20 - Cursos USP Sistema Terra"),
    ("WyPpVXVv-74","21 - Cursos USP Sistema Terra"),
    ("C5Wohy9vMrM","22 - Cursos USP Sistema Terra"),
    ("rhSUu5dwBDk","23 - Cursos USP Sistema Terra"),
    ("vGIHhnUtAqQ","24 - Cursos USP Sistema Terra"),
    ("aD6txgHn1po","25 - Cursos USP Sistema Terra"),
    ("AZhfhHKFNF8","26 - Cursos USP Sistema Terra"),
]

PLAYLIST_POR_AULA = [
    ("l1GEc19CMG0","Aula 01 parte 1 - Introducao"),
    ("yMRPyYOjzj4","Aula 01 parte 2 - Introducao"),
    ("-By4afePoEc","Aula 01 parte 3 - Introducao"),
    ("4Wh09aMx2GE","Aula 02 parte 1 - Tectonica de Placas"),
    ("_HYC-JPu7eA","Aula 02 parte 2 - Tectonica de Placas"),
    ("yPObdJb1GX4","Aula 02 parte 3 - Tectonica de Placas"),
    ("yn925BEavig","Aula 03 parte 1 - Evolucao do Pensamento Geocientifico"),
    ("cdIyrNewmuI","Aula 03 parte 2 - Evolucao do Pensamento Geocientifico"),
    ("7gk-lngPtFE","Aula 03 parte 3 - Evolucao do Pensamento Geocientifico"),
    ("nCCexhTZcjQ","Aula 04 parte 1 - Minerais"),
    ("UEXpAfQdBoU","Aula 04 parte 2 - Minerais"),
    ("PxwGY_4CHxg","Aula 05 parte 1 - Processos formadores de rochas"),
    ("6XpHdV-tI0A","Aula 05 parte 2 - Processos formadores de rochas"),
    ("ZIbA2h7L7V8","Aula 06 parte 1 - Rochas Igneas"),
    ("WYaJJQQ5niw","Aula 06 parte 2 - Rochas Igneas"),
    ("o5KSF7Y2iUQ","Aula 06 parte 3 - Rochas Igneas"),
    ("mnnYLLk479M","Aula 07 parte 1 - Rochas Sedimentares"),
    ("In3I99PwtX8","Aula 07 parte 2 - Rochas Sedimentares"),
    ("LDH9eY5ZN6M","Aula 07 parte 3 - Rochas Sedimentares"),
    ("jpwZogmhY4M","Aula 08 parte 1 - Rochas Metamorficas"),
    ("m8JXSBJ8NCw","Aula 08 parte 2 - Rochas Metamorficas"),
    ("il67ZThLqc4","Aula 09 parte 1 - Ciclo das Rochas e Estruturas"),
    ("xaq71ndyLg4","Aula 09 parte 2 - Ciclo das Rochas e Estruturas"),
    ("b0qOm9RizN8","Aula 09 parte 3 - Ciclo das Rochas e Estruturas"),
    ("1j7a3Q4Ufyg","Aula 10 parte 1 - Ciencias da Terra e o Tempo Geologico"),
    ("-fhes96EED8","Aula 10 parte 2 - Ciencias da Terra e o Tempo Geologico"),
]

PLAYLIST_RICARDO = [
    ("oIUTIClodKU","Eras Geologicas (aula completa)"),
    ("JTma-7fu-eA","Tipos de Rochas (aula completa)"),
    ("r2nP_S9Milc","Geomorfologia - Agentes Internos do Relevo"),
    ("LiV76HMsE0I","Geomorfologia - Agentes Externos do Relevo"),
    ("E3lOxx6e_D8","Relevo do Brasil (aula completa)"),
    ("ZAygYHX1e0o","Relevo de Sao Paulo (aula completa)"),
]

def main():
    folder_num = os.path.join(BASE, "Sistema-Terra-USP", "Playlist-Numerada")
    folder_aula = os.path.join(BASE, "Sistema-Terra-USP", "Playlist-Por-Aula")
    folder_ric = os.path.join(BASE, "Geologia-Geomorfologia-Ricardo-Marcilio")

    for vid, title in PLAYLIST_NUMERADA:
        process(vid, slugify(title) + ".txt", folder_num)
    for vid, title in PLAYLIST_POR_AULA:
        process(vid, slugify(title) + ".txt", folder_aula)
    for vid, title in PLAYLIST_RICARDO:
        process(vid, slugify(title) + ".txt", folder_ric)

if __name__ == "__main__":
    main()
