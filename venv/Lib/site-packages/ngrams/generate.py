import csv
import os

class Ngrams(object):

    def __init__(self):
        pass

    def result(self, number):
        result = []
        with open('{0}/ngrams/ngrams{1}.csv'.format(os.getcwd(), number), 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                result.append(row[0].split(','))
        return result
