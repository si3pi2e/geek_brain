'''https://www.weatherapi.com/docs/ retestforewer@gmail.com Ramakrishnaj'''
import requests
import json
from random import choice


def send_req(url, query):
    response = requests.get(url=url, params=query)
    return response.json()


def write_to_file(data):
    with open('respons.json', 'w') as file:
        file.write(json.dumps(data, indent=4))


base_url = 'http://api.weatherapi.com/v1/current.json?'
api_key = '07db26a138674e43b7e211650231202'
city = choice(['London', 'Paris', 'Beijing'])
params_data = {'key': api_key, 'q': city, 'aqi': 'yes'}


if __name__ == '__main__':
    write_to_file(send_req(base_url, params_data))
