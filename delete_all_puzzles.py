import json
import requests

# get all puzzles

headers = {
    'X-CSRFToken': 'qtbUZJe1cqMmkqbTzLOJSrkKFlzBPz9HpzaYtjJegqALr1xfwmE7xB3ikUIT5RDL',
    'cookie': 'csrftoken=qtbUZJe1cqMmkqbTzLOJSrkKFlzBPz9HpzaYtjJegqALr1xfwmE7xB3ikUIT5RDL; sessionid=v7iyw3tdrz8cvpdoj9yj45km27cjaefb',
    'content-type': 'application/json'
}

r = requests.get(
    'http://localhost:8000/api/v1/hunts/1/puzzles',
    headers=headers)

data = r.json()
while len(data) > 0:
    print(str(len(data)) + " puzzles to delete")

    for puz in data:
        id = puz['id']
        requests.delete(
            f'http://localhost:8000/api/v1/hunts/1/puzzles/{id}',
            headers=headers)

    r = requests.get(
        'http://localhost:8000/api/v1/hunts/1/puzzles',
        headers=headers)
    data = r.json()
