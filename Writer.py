import csv



class Writer(object):
    def csv_writer (data, path):
        with open("resultpars.csv", 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow((data['div'],
                             data['meta'],
                             data['link']))
        path = "resultpars.csv"
        data.csv_writer(data)


