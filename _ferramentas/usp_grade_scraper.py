"""
Scraper generico para grade curricular e disciplinas do Jupiterweb (USP).

Uso:
    python3 usp_grade_scraper.py --codcg 44 --codcur 44011 --codhab 100 --out "../GradeCurricular/Geologia-USP"

Reusavel para qualquer curso da USP: basta trocar codcg/codcur/codhab (e opcionalmente tipo).
Esses codigos aparecem na propria URL da grade curricular do Jupiterweb, ex:
https://uspdigital.usp.br/jupiterweb/listarGradeCurricular?codcg=44&codcur=44011&codhab=100&tipo=N

O que o script faz:
1. Baixa a pagina da grade curricular e extrai todos os codigos de disciplina (sgldis) referenciados,
   junto com a categoria (Obrigatoria / Optativa Livre / Optativa Eletiva) e o periodo ideal, quando aplicavel.
2. Para cada disciplina, baixa a pagina "obterDisciplina" (versao print=true) e extrai:
   codigo, nome (PT e EN), creditos, carga horaria, ementa, objetivos, conteudo programatico,
   metodos de ensino, avaliacao, bibliografia.
3. Salva cada disciplina como um .md limpo, organizado em subpastas por categoria.
4. Salva um indice geral (grade.json e grade.md) com a estrutura completa da grade.

Sem uso de LLM: extracao 100% deterministica via regex/HTML parsing.
"""
import argparse
import html
import json
import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://uspdigital.usp.br/jupiterweb"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; curriculo-scraper/1.0)"}


def slugify(name, maxlen=90):
    name = name.strip()
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    name = re.sub(r'\s+', ' ', name)
    return name[:maxlen].strip()


def fetch(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            r = requests.get(url, headers=HEADERS, timeout=30)
            if r.status_code == 200:
                r.encoding = "windows-1252"
                return r.text
        except requests.RequestException:
            pass
        time.sleep(delay)
    return None


def parse_grade(codcg, codcur, codhab, tipo="N"):
    """Retorna lista de dicts: {codigo, nome, categoria, periodo}."""
    url = f"{BASE_URL}/listarGradeCurricular?codcg={codcg}&codcur={codcur}&codhab={codhab}&tipo={tipo}"
    text = fetch(url)
    if text is None:
        raise RuntimeError(f"Falha ao baixar grade curricular: {url}")

    soup = BeautifulSoup(text, "html.parser")
    disciplinas = []
    seen = set()

    categoria_atual = "Obrigatoria"
    periodo_atual = None

    for el in soup.find_all(["td", "b", "font"]):
        txt = el.get_text(" ", strip=True)
        if not txt:
            continue
        if "Disciplinas Obrigat" in txt:
            categoria_atual = "Obrigatoria"
        elif "Optativa Livre" in txt:
            categoria_atual = "Optativa Livre"
        elif "Optativa Eletiva" in txt:
            categoria_atual = "Optativa Eletiva"
        m = re.match(r'^(\d+)[ºo]\s*Per[ií]odo Ideal', txt)
        if m:
            periodo_atual = int(m.group(1))

    for a in soup.find_all("a", href=re.compile(r"obterDisciplina\?sgldis=")):
        href = a["href"]
        m = re.search(r"sgldis=([A-Za-z0-9]+)", href)
        if not m:
            continue
        codigo = m.group(1)
        if codigo in seen:
            continue
        row = a.find_parent("tr")
        nome = ""
        categoria = None
        periodo = None
        if row:
            tds = row.find_all("td")
            if len(tds) > 1:
                nome = tds[1].get_text(" ", strip=True)
            # busca categoria/periodo olhando as linhas anteriores da tabela
            prev = row.find_previous(["td", "b"])
            # scan reverso pelo html bruto para pegar contexto real de secao/periodo
        seen.add(codigo)
        disciplinas.append({
            "codigo": codigo,
            "nome": nome,
        })

    # segunda passada: normaliza todo o whitespace (headings e codigos podem ter
    # quebras de linha internas nos proprios nos de texto) e usa offset de caractere
    # para atribuir categoria/periodo corretamente por posicao no documento.
    raw = soup.get_text(" ", strip=False)
    plain = re.sub(r'\s+', ' ', raw)

    codigos_validos = {d["codigo"] for d in disciplinas}
    idx_by_code = {}
    for m in re.finditer(r'(?<![A-Za-z0-9])([A-Z0-9]{4,7})(?![A-Za-z0-9])', plain):
        code = m.group(1)
        if code in codigos_validos and code not in idx_by_code:
            idx_by_code[code] = m.start()

    cat_marks = []
    for m in re.finditer(r'Disciplinas Obrigat', plain):
        cat_marks.append((m.start(), "Obrigatoria"))
    for m in re.finditer(r'Disciplinas Optativas? Livres?', plain):
        cat_marks.append((m.start(), "Optativa Livre"))
    for m in re.finditer(r'Disciplinas Optativas? Eletivas?', plain):
        cat_marks.append((m.start(), "Optativa Eletiva"))
    cat_marks.sort()

    per_marks = []
    for m in re.finditer(r'(\d+)[ºo] Per[ií]odo Ideal', plain):
        per_marks.append((m.start(), int(m.group(1))))
    per_marks.sort()

    def mark_before(marks, pos, default=None):
        val = default
        for i, v in marks:
            if i <= pos:
                val = v
            else:
                break
        return val

    for d in disciplinas:
        pos = idx_by_code.get(d["codigo"])
        if pos is not None:
            d["categoria"] = mark_before(cat_marks, pos, "Obrigatoria")
            d["periodo"] = mark_before(per_marks, pos, None)
        else:
            d["categoria"] = "Referenciada (pre-requisito)"
            d["periodo"] = None

    return disciplinas


FIELD_LABELS = [
    ("ementa", "Ementa"),
    ("objetivos", "Objetivos"),
    ("conteudo_programatico", "Conteúdo Programático"),
    ("metodos_ensino", "Métodos de Ensino"),
    ("metodo_avaliacao", "Método de Avaliação"),
    ("criterio_avaliacao", "Critério de Avaliação"),
    ("norma_recuperacao", "Norma de Recuperação"),
    ("bibliografia_basica", "Bibliografia Básica"),
    ("bibliografia_complementar", "Bibliografia Complementar"),
]


def parse_disciplina(codigo, codcur, codhab):
    url = f"{BASE_URL}/obterDisciplina?sgldis={codigo}&codcur={codcur}&codhab={codhab}&print=true"
    text = fetch(url)
    if text is None:
        return None
    soup = BeautifulSoup(text, "html.parser")

    data = {"codigo": codigo, "url": url}

    # nome PT / EN: duas linhas em negrito logo apos "Disciplina: CODIGO - NOME"
    body_text = soup.get_text("\n", strip=True)
    m = re.search(r'Disciplina:\s*' + re.escape(codigo) + r'\s*-\s*([^\n]+)', body_text)
    if m:
        data["nome_pt"] = m.group(1).strip()
    lines = body_text.split("\n")
    if m:
        idx = next((i for i, l in enumerate(lines) if l.strip().startswith(f"Disciplina: {codigo}")), None)
        if idx is not None and idx + 1 < len(lines):
            candidate = lines[idx + 1].strip()
            # nome em ingles normalmente vem logo em seguida, numa linha separada, sem rotulo
            if candidate and not any(lbl in candidate for _, lbl in FIELD_LABELS) and "Créditos" not in candidate:
                data["nome_en"] = candidate

    for key, label in FIELD_LABELS:
        m = re.search(re.escape(label) + r'\s*\n?(.*?)(?=\n(?:' + "|".join(re.escape(l) for _, l in FIELD_LABELS) + r')|\Z)', body_text, re.S)
        if m:
            val = m.group(1).strip()
            val = re.sub(r'\n{2,}', '\n', val)
            if val:
                data[key] = val

    for label, key in [("Créditos Aula:", "creditos_aula"), ("Créditos Trabalho:", "creditos_trabalho"),
                        ("Carga Horária Total:", "carga_horaria_total"), ("Tipo:", "tipo")]:
        m = re.search(re.escape(label) + r'\s*\n?\s*([^\n]+)', body_text)
        if m:
            data[key] = m.group(1).strip()

    return data


def disciplina_to_markdown(d):
    lines = [f"# {d['codigo']} - {d.get('nome_pt', '')}"]
    if d.get("nome_en"):
        lines.append(f"*{d['nome_en']}*")
    lines.append("")
    lines.append(f"URL: {d['url']}")
    lines.append("")
    meta_bits = []
    for key, label in [("creditos_aula", "Créditos Aula"), ("creditos_trabalho", "Créditos Trabalho"),
                        ("carga_horaria_total", "Carga Horária"), ("tipo", "Tipo")]:
        if d.get(key):
            meta_bits.append(f"**{label}:** {d[key]}")
    if meta_bits:
        lines.append(" | ".join(meta_bits))
        lines.append("")
    for key, label in FIELD_LABELS:
        if d.get(key):
            lines.append(f"## {label}")
            lines.append(d[key])
            lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--codcg", required=True)
    ap.add_argument("--codcur", required=True)
    ap.add_argument("--codhab", required=True)
    ap.add_argument("--tipo", default="N")
    ap.add_argument("--out", required=True)
    ap.add_argument("--incluir-referenciadas", action="store_true",
                     help="Tambem baixa disciplinas que aparecem so como pre-requisito de outra")
    ap.add_argument("--delay", type=float, default=0.5)
    args = ap.parse_args()

    out_dir = os.path.abspath(args.out)
    os.makedirs(out_dir, exist_ok=True)

    print("Baixando grade curricular...")
    disciplinas = parse_grade(args.codcg, args.codcur, args.codhab, args.tipo)
    print(f"{len(disciplinas)} disciplinas encontradas na grade.")

    with open(os.path.join(out_dir, "grade.json"), "w", encoding="utf-8") as f:
        json.dump(disciplinas, f, ensure_ascii=False, indent=2)

    for d in disciplinas:
        cat = d["categoria"]
        if cat == "Referenciada (pre-requisito)" and not args.incluir_referenciadas:
            print(f"SKIP (so pre-requisito, use --incluir-referenciadas para pegar): {d['codigo']}")
            continue
        cat_folder = slugify(cat)
        folder = os.path.join(out_dir, cat_folder)
        os.makedirs(folder, exist_ok=True)
        fname = f"{d['codigo']} - {slugify(d['nome'] or d['codigo'])}.md"
        fpath = os.path.join(folder, fname)
        if os.path.exists(fpath):
            print(f"SKIP (existe): {fname}")
            continue
        detail = parse_disciplina(d["codigo"], args.codcur, args.codhab)
        if detail is None:
            print(f"FAIL: {d['codigo']}")
            continue
        md = disciplina_to_markdown(detail)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"OK: {fname}")
        time.sleep(args.delay)

    print("Concluido.")


if __name__ == "__main__":
    main()
