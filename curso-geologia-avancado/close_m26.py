#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import yaml

# Read YAML
with open('course-state.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# Get module 26 (at index 26)
module26 = data['modules'][26]

# Update status
module26['status'] = 'completed'

# Update flashcards
module26['flashcards'] = {
    'generated_at': '2026-09-22',
    'format': ['csv', 'markdown'],
    'cards': 100,
    'validation': {
        'status': 'passed',
        'errors': 0,
        'warnings': 1,
        'note': 'Baralho de 100 cards com fatos-chave das 7 aulas. Validacao: 0 erros, 1 aviso (near_duplicate).'
    }
}

# Update global state
data['current_module'] = 27
data['next_action'] = 'Modulo 27 (petrocronologia): redacao de aulas via geo-redator'

# Write YAML with CRLF
yaml_str = yaml.safe_dump(data, default_flow_style=False, allow_unicode=True, width=120)
yaml_str = yaml_str.replace('\n', '\r\n')

with open('course-state.yaml', 'w', encoding='utf-8-sig', newline='') as f:
    f.write(yaml_str)

print("Module 26 closed in YAML")
print("  status: completed")
print("  flashcards: 100 cards")
print("  current_module: 27")
