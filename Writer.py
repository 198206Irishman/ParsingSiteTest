import csv



class Writer(object):
    def csv_read (data):
        with open("data.csv", 'a') as file:
            writer = csv.writer(file)
            writer.writerow((data['head'], data['link']))
    pass


Writer