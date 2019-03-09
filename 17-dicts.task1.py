import requests
import random
import easygui

langs = [
    'ru',
    'en',
    'ВЫЙТИ'
]

while True:
    l = easygui.buttonbox(msg='Выбери язык', title='Выбор языка ', choices=(langs))
    if l == 'ВЫЙТИ':
        break
    ir = random.randint(1, 999999)
    url = 'http://api.forismatic.com/api/1.0/'
    payload = {'method': 'getQuote', 'format': 'json', 'key': ir, 'lang': l}
    res = requests.get(url, params=payload)
    data = res.json()
    easygui.msgbox(data['quoteText'])
