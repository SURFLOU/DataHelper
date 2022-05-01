import matplotlib.pyplot as plt
import seaborn as sns
from spreadsheets import CSVFile
import pandas as pd


class Plot:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data
        self.chartX = []
        self.chartY = []
        for elems in self.data:
            self.chartX.append(elems[0])
            self.chartY.append(elems[2])

        self.df = pd.DataFrame(self.data, columns=[self.x, self.y])
        self.df = self.df.astype({self.y: int}, errors='raise')

    def MakeBarPlot(self, style):
        sns.set_style(style)
        sns.barplot(x=self.x, y=self.y, data=self.df)
        plt.show()

    def MakePiePlot(self):
        colors = sns.color_palette('pastel')[0:5]
        plt.pie(self.chartY, labels=self.chartX, colors=colors, autopct='%.0f%%')
        plt.show()

CSV = CSVFile("panstwa.csv")
data = CSV.readHeaders() + CSV.readRows()
Wykres = Plot("Panstwo", "Populacja", data)
Wykres.MakePiePlot()