#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re

sites = [
    ('https://stackshare.io/', 'stackshare.io_.html'),
    ('https://aappss.ru/', 'aappss.ru_.html'),
    ('https://devfolio.co/', 'devfolio.co_.html'),
    ('https://www.futuretools.io/submit', 'futuretools_submit.html'),
    ('https://betalist.com/', 'betalist.com_.html'),
    ('https://pitchwall.co/submit', 'pitchwall_submit.html'),
    ('https://www.launchingnext.com/submit', 'launchingnext_submit.html')
]

for url, filename in sites:
    print(f'\n=== {url} ===')
    try:
        r = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        print(f'Status: {r.status_code}')

        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')

            # Ищем формы
            forms = soup.find_all('form')
            if forms:
                print(f'✓ Found {len(forms)} form(s)')

                for i, form in enumerate(forms):
                    action = form.get('action', 'no action')
                    method = form.get('method', 'get')
                    print(f'  Form {i+1}: {method} → {action}')

                    # Поля формы
                    inputs = form.find_all(['input', 'textarea', 'select'])
                    print(f'    Fields: {len(inputs)}')
                    for inp in inputs[:10]:  # Первые 10 полей
                        name = inp.get('name', 'no name')
                        inp_type = inp.get('type', inp.name)
                        placeholder = inp.get('placeholder', '')
                        if placeholder:
                            print(f'      - {inp_type}: {name} ({placeholder})')
                        else:
                            print(f'      - {inp_type}: {name}')
            else:
                # Ищем ссылки на submission
                submit_links = soup.find_all('a', href=re.compile(r'submit|add|post|create', re.I))
                if submit_links:
                    print(f'✓ Found {len(submit_links)} submission link(s):')
                    for link in submit_links[:5]:
                        href = link.get('href', '')
                        text = link.get_text(strip=True)[:50]
                        print(f'  → {text}: {href}')

            # Сохраняем HTML
            with open(filename, 'w') as f:
                f.write(str(soup.prettify())[:100000])
            print(f'→ Saved: {filename}')

    except Exception as e:
        print(f'✗ Error: {e}')
