# _*_ coding: utf-8 _*_
from bs4 import BeautifulSoup
import urlopen




class ParSite(object):
    def html_doc (soup):
        html_doc = urlopen('http://').read()
        soup = BeautifulSoup(html_doc)
        #print(soup)
        #print(soup.title)
        #print(soup.title.string)
        for meta in soup.find_all('meta'):
            meta.get('content')
        for link in soup.find_all('a'):
            link.get('href')
        for link in soup.find_all('a'):
            link.contents[0]
        soup.find('div', 'content')
        soup.find('div', id='top_menu')







