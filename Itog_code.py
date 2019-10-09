import sys
from bs4 import BeautifulSoup
import lxml
from urllib import request
import csv
import requests


class itogcode (object):
    def get_html(self, url):
        self.response = requests.get(url)
        self.response.encoding = 'utf8'
        return self.response.text

    # Записываем данные файл
    def csv_read(data):
        with open("resultspars.csv", 'a') as file:
            writer = csv.writer(file)
            writer.writerow((data['head'],
                             data['link']))

    def get_link(html):
        soup = BeautifulSoup(html, 'lxml')
        head = soup.find('div', id='section-content').find_all('a', class_="entry-header")
        for i in head:
            link = 'https://3dnews' + i.get('href')
            heads = i.find('h1').string

        data = {'head': heads,
                'link': link}

        data.csv_read(data)


    data = get_link(get_html('https://3dnews/news'))
