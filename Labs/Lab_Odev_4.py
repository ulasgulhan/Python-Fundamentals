
import requests

while True:
    country = input('Ülkenin hava durumu: ').title()
    if country == 'Exit':
        print('Çıkış yapılıyor')
        break
    else:
        api = requests.get(f'http://api.weatherapi.com/v1/current.json?key=fac9213163234deba08182647230411 &q={country}&aqi=no')

        response = api.json()

        derece = response['current']['temp_c']
        sehir = response['location']['name']

        print(f'{sehir}: {derece} derece')
