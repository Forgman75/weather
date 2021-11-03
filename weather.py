# -*- coding: utf-8 -*-
import requests

cities = ["Лондон","Шереметьево","Череповец"]
place = ''
baseurl = 'https://wttr.in/'
param = '?nTq&lang=ru'
def get_weather(place):
    url = baseurl + place + param
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)

for i, place in enumerate(cities):
    get_weather(place)

