from random import choice
import requests
import json


def send_req(url: str):
    response = requests.get(url=url)
    return response.json()


def write_to_file(usr: str, data):
    with open(f'repo_{usr}.json', 'w') as file:
        file.write(json.dumps(data, indent=4))


user = choice(['geekan', 'DJWOMS', 'octocat'])
# user = input("Enter name user on GitHub")

url_api = 'https://api.github.com'
path_repo = f'/users/{user}/repos'

if __name__ == '__main__':
    write_to_file(user, send_req(url_api + path_repo))
