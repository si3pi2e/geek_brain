from random import choice
import requests


def send_req(url: str):
    response = requests.get(url=url)
    resp_dict_list = response.json()
    repo_list = []
    for item in resp_dict_list:
        repo_list.append(item['name'])
    return repo_list


def parse_name_repositories_to_file(usr: str, data: list):
    with open(f'repo_{usr}.txt', 'w') as file:
        file.write(f'У пользователя GitHub "{usr}" имеются следующие репозитории:\n')
        file.write('\n'.join(data))


users_list = ['geekan', 'DJWOMS', 'octocat']
user = choice(users_list)
# user = input("Enter name user on GitHub")

url_api = 'https://api.github.com'
path_user = f'/users/{user}'
path_repo = f'/users/{user}/repos'

if __name__ == '__main__':
    parse_name_repositories_to_file(user, send_req(url_api+path_repo))
