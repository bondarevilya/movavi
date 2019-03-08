import requests
import random

ir = random.randint(1, 999999)

url = 'http://api.forismatic.com/api/1.0/'
payload = {'method': 'getQuote', 'format': 'json', 'key': ir, 'lang': 'ru'}
res = requests.get(url, params=payload)

data = res.json()

print(data)
print(payload)
