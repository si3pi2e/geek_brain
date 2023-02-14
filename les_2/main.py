# -*- coding: utf-8 -*-
import requests
from lxml import html
import json


def main():
    '''Написать приложение или функцию, которые собирают основные новости с сайта
    на выбор lenta.ru, yandex-новости. Для парсинга использовать XPath.
    Структура данных в виде словаря должна сожержать:
    - *название источника;
    - наименование новости;
    - ссылку на новость;
    - дата публикации.
    Минимум один сайт, максимум - все два.'''
    pass


def send_request(url):
    headers = {
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}
    response = requests.get(url, headers=headers)
    return response.content


def parse_news(content):
    path = "//a[contains(@class, 'card-mini _topnews')]"
    root = html.fromstring(content)
    news = root.xpath(path)
    news_dict = {}

    for new in news:
      title = new.xpath(".//span")[0].text
      href = new.attrib['href']
      date = '-'.join(href.split('/')[2:5])+ ' ' + new.xpath(".//time")[0].text
      news_dict[title] = (title, date, url + href)

    return news_dict


url = 'https://lenta.ru'
content = send_request(url)
tottal_news = parse_news(content)
print(tottal_news)

