from .metaData import MetaData
import matplotlib.pyplot as plt


class Plotting(MetaData):

    def __init__(self):
        super().__init__()

    def prices(self):
        print(self.dataFrame)
        self.dataFrame.plot(figsize=(12, 8))
        plt.show()
