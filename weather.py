import requests

def main():
    cities = ["Лондон", "Шереметьево", "Череповец",]
    params = {'n':'', 'T':'', 'q':'', 'lang':'ru'}

    for place in cities:
        url = "https://wttr.in/{p}".format(p=place)
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(response.text)


if __name__ == "__main__": 
    main() 


