from ParSite import *
from Writer import *

if __name__ == '__main__':
    print("http://", input('http://'))
    http = ParSite()
    http.html_doc('http://')

    data = Writer()
    data.csv_writer(data)
    #data = link.get(get.html('https://33pingvina.ru'))
