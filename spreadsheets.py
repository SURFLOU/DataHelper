import csv
import re


class CSVFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename)
        self.csvreader = csv.reader(self.file)
        self.header = next(self.csvreader)

    def readRows(self):
        rows = []
        for row in self.csvreader:
            row[0] = row[0].replace(';', ' ')
            rows.append(row[0].split())
        return rows

    def readHeaders(self):
        tab = [self.header[0].split(";")]
        return tab

    def closeFile(self):
        self.file.close()


