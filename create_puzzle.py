import json
import requests

headers = {
    'X-CSRFToken': 'qtbUZJe1cqMmkqbTzLOJSrkKFlzBPz9HpzaYtjJegqALr1xfwmE7xB3ikUIT5RDL',
    'cookie': 'csrftoken=qtbUZJe1cqMmkqbTzLOJSrkKFlzBPz9HpzaYtjJegqALr1xfwmE7xB3ikUIT5RDL; sessionid=v7iyw3tdrz8cvpdoj9yj45km27cjaefb',
    'content-type': 'application/json'
}

payload = {
    'name': 'testcreatepuz1',
    'url': 'testcreatepuzurl1.com',
    'is_meta': False
}

r = requests.post(
    'http://localhost:8000/api/v1/hunts/1/puzzles',
    data=json.dumps(payload),
    headers=headers)

print(r.text)
