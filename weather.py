# -*- coding: utf-8 -*-
import requests

cities = ["Лондон","Шереметьево","Череповец"]
place = ''
param = {'n':'', 'T':'', 'q':'', 'lang':'ru'}
def get_weather(place):
    url = "https://wttr.in/{p}".format(p=place)
    response = requests.get(url, params=param)
    response.raise_for_status()
    print(response.text)

for place in cities:
    get_weather(place)

