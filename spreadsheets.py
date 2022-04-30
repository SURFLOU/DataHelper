import csv
import re


class CSVFile:
    def __init__(self, filename, header):
        self.filename = filename
        self.header = header
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
        return self.header[0].split(";")

    def closeFile(self):
        self.file.close()


CSV = CSVFile("wakacje.csv", 'miasto')
print(CSV.readHeaders())
print(CSV.readRows())
