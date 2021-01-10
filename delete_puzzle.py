import json
import requests

headers = {
    'X-CSRFToken': 'qtbUZJe1cqMmkqbTzLOJSrkKFlzBPz9HpzaYtjJegqALr1xfwmE7xB3ikUIT5RDL',
    'cookie': 'csrftoken=qtbUZJe1cqMmkqbTzLOJSrkKFlzBPz9HpzaYtjJegqALr1xfwmE7xB3ikUIT5RDL; sessionid=v7iyw3tdrz8cvpdoj9yj45km27cjaefb',
    'content-type': 'application/json'
}

r = requests.delete(
    'http://localhost:8000/api/v1/hunts/1/puzzles/26',
    headers=headers)

print(r.status_code)
print(r.text)
