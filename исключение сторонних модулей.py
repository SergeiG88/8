import requests

url = 'http://ya.ru'
try:
    data = requests.get(url)
    print(data.text)
except requests.ConnectionError as exc:
    print(f'не могу соедиться с {url} потому что {exc}')
