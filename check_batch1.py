#!/usr/bin/env python3
import requests
import re

sites = [
    'https://stackshare.io/',
    'https://aappss.ru/',
    'https://devfolio.co/projects/bitdive-7040',
    'https://www.futuretools.io/',
    'https://betalist.com/',
    'https://pitchwall.co/',
    'https://www.launchingnext.com/'
]

for site in sites:
    print(f'\n=== {site} ===')
    try:
        r = requests.get(site, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        print(f'Status: {r.status_code}')
        if r.status_code == 200:
            # Ищем форму сабмишна
            if 'submit' in r.text.lower() or 'add' in r.text.lower():
                print('✓ Has submission/add form detected')
            # Сохраним для анализа
            filename = site.replace('https://', '').replace('http://', '').replace('/', '_')[:50] + '.html'
            with open(filename, 'w') as f:
                f.write(r.text[:50000])
            print(f'→ Saved: {filename}')
    except Exception as e:
        print(f'✗ Error: {e}')
