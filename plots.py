import matplotlib.pyplot as plt
import seaborn as sns
from spreadsheets import CSVFile
import pandas as pd


class Plot:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data
        self.df = pd.DataFrame(self.data, columns=[self.x, self.y])
        self.df = self.df.astype({self.y: int}, errors='raise')

    def MakeBarPlot(self, style):
        sns.set_style(style)
        sns.barplot(x=self.x, y=self.y, data=self.df)
        plt.show()


CSV = CSVFile("wakacje.csv")
rows = CSV.readRows()
Wakacje = Plot("Miasta", "Suma", rows)
Wakacje.MakeBarPlot('darkgrid')
