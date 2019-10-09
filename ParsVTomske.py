import requests
from lxml import html
import csv
class Pars():
    def http_link(self):
        self.response = requests.get('http://vtomske.ru')
        self.response.enconding = 'utf8'
        self.parsed_body = html.fromstring(self.response.text)
        #print(response.headers)
        #print(response.request.headers)
        self.head = (self.parsed_body.xpath('//title/text()'))
        self.link = (self.parsed_body.xpath('//a/@href'))
        self.http_link(self)
def csv_writer (data, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in data:
            writer.writerow(line)

if __name__ == "__main__":
    data = {'head': head,
            'link': link}
    path = "results.csv"
    csv_writer(data, path)








