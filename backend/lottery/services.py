import json
from urllib import request
import requests
from datetime import date

def generate_request(url, params={}, headers={}):
    response = requests.get(url, params=params, headers=headers)
    urls = response.url
    if response.status_code == 200:
        return response

def get_username(params={}):
    response = generate_request('https://randomuser.me/api', params)
    if response:
       user = response.get('results')[0]
       return user.get('name').get('first')

    return ''

'''url = "https://loterias-y-quinielas-argentinas.p.rapidapi.com/loterias"

    headers = {
        'x-rapidapi-host': "loterias-y-quinielas-argentinas.p.rapidapi.com",
        'x-rapidapi-key': "48254b2193msh3029a16c7581387p162d63jsn9b236e661017"
        }
    #response = requests.request("GET", url, headers=headers)
    response =generate_request(headers=headers)
    response_json = json.loads(response)
'''
def get_lotteries_payed_api( ):
    # Harcoded response
    with open("C:/DjangoTest/django-todo-react/backend/lottery/response_loterias_api.json", 'r',encoding = 'utf-8') as response_file:
        response = response_file.read()
    if response:
        response = json.loads(response)
        return response

def get_lotteries( ):
    url = "https://api.elpais.com/ws/LoteriaNavidadPremiados"
    #?sorteo=2022/01/QNL51P20220125.xml
    params = {'n' : 'resumen' }
    response = generate_request(url, params )
    response_decode = response.content.decode()
    if response_decode:
        response_decode = response_decode.strip('premios=')
        return json.loads(response_decode)
