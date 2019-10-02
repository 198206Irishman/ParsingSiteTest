# _*_ coding: utf-8 _*_
from bs4 import BeautifulSoup
import urlopen




class ParSite(object):
    def html_doc (soup):
        html_doc = urlopen('http://33pingvina.ru').read()
        soup = BeautifulSoup(html_doc)
        #print(soup)
        #print(soup.title)
        #print(soup.title.string)
        for meta in soup.find_all('meta'):
            print(meta.get('content'))



    pass



