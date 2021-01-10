import json
import re
import requests
import sys

headers = {
    'X-CSRFToken': 'qtbUZJe1cqMmkqbTzLOJSrkKFlzBPz9HpzaYtjJegqALr1xfwmE7xB3ikUIT5RDL',
    'cookie': 'csrftoken=qtbUZJe1cqMmkqbTzLOJSrkKFlzBPz9HpzaYtjJegqALr1xfwmE7xB3ikUIT5RDL; sessionid=v7iyw3tdrz8cvpdoj9yj45km27cjaefb',
    'content-type': 'application/json'
}

count = 0

with open('pb6puzzles.txt') as f:
    for line in f:
        line = line.strip()
        parts = re.split(r'\s*,\s*', line)
        puzzle = parts[0]
        meta = parts[1]
        has_meta = True if meta else False
        is_meta = True if parts[2] == 'yes' else False

        print('Processing: ' + puzzle + ',' + str(has_meta) + ',' + meta + ',' + str(is_meta))

        payload = {
            'name': puzzle,
            'url': puzzle,
            'is_meta': is_meta
        }

        r = requests.post(
                'http://localhost:8000/api/v1/hunts/1/puzzles',
                data=json.dumps(payload),
                headers=headers
            )

        if r.status_code != 200:
            print('ERROR!: ' + str(r.text))
            sys.exit(1)

        data = r.json()

        puz_id = data['id']

        if has_meta:
            # add tag
            payload = {
                'name': meta,
                'color': 'dark'
            }

            r = requests.post(
                f'http://localhost:8000/api/v1/puzzles/{puz_id}/tags',
                data=json.dumps(payload),
                headers=headers
            )

            if r.status_code != 200:
                print('ERROR!: ' + str(r.text))
                sys.exit(1)

        count += 1

        # if count == 20:
            # break

print('added', count, 'puzzles')
