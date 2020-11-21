from .metaData import MetaData
from .plotting import Plotting


class Display:
    def __init__(self):
        self.tickers = ['FB', 'GOOG', 'AMZN', 'INRG.MI']
        self.start = '01-01-2018'
        self.end = '01-01-2020'
        self.metaData = MetaData()
        self.plotting = Plotting(self.metaData)
        self.allocation = None

    def give_menu_of_options(self):
        options = ['1', '2', '3', '4']
        text = None
        print("\n\n     Hey Hey\n\n")
        while text not in options:
            text = input(
                'Choose from the following\n1) Show Tickers\n2) Get Tickers\n3) Portfolio Descriptive Statistics\n\n')
            if text == '1':
                self.show_tickers()
            elif text == '2':
                self.ask_for_tickers()
            elif text == '3':
                self.descriptive_stat_walkthrough()

    # Option 1
    def show_tickers(self):
        print("\n\n", self.tickers)

    # Option 2
    def ask_for_tickers(self):
        tickers = []
        text = None
        while text != "Finish":
            text = input('\n\nType Finish When Done\nEnter Stock Tickers\n')
            if text != '' and text != "Finish":
                tickers.append(text.upper())
        self.tickers = tickers
        return self.tickers

    # Option 3
    def descriptive_stat_walkthrough(self):
        options = ['1', '2']
        text = None
        while text not in options:
            text = input('1) Stats 2) Plotting \n')
            if text == '1':
                self.show_descriptive_stats()
            elif text == '2':
                print('To be made')
            else:
                break

    # 3a - Descriptive Statistics
    def show_descriptive_stats(self):
        self.metaData.get(self.tickers, start=self.start,
                          end=self.end)
        av_ret, pair_cov, correl = metaData.descriptive_statistics()
        print('\n---Average Return---\n\n', av_ret)
        print('\n\n---Pairwise Covariance---\n\n', pair_cov)
        print('\n\n---Correlation Matrix---\n\n', correl)

    # 3b - Plotting
    def plotting_walkthrough():
        options = ['1', '2']
        text = None
        while text not in options:
            print('Not Working Yet')
