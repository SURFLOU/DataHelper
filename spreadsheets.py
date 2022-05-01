import csv
import pandas as pd


class CSVFile:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.file = open(self.filename)
            self.csvreader = csv.reader(self.file)
            self.header = next(self.csvreader)
        except FileNotFoundError:
            self.file = open(self.filename, 'w')

    def writeToFile(self, data):
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(self.file)
            writer.writerows(data)

    def readRows(self):
        rows = []
        for row in self.csvreader:
            rows.append(row)
        return rows

    def readHeaders(self):
        tab = []
        tab.append([self.header[0],self.header[1],self.header[2]])
        return tab

    def makeDataframe(self):
        return pd.read_csv(self.filename)

    def closeFile(self):
        self.file.close()




