from .metaData import MetaData
from .plotting import Plotting
from .monteCarlo import MonteCarlo
from .dataCollection import DataCollection
from .readCSV import ReadCSV


class Display:
    def __init__(self):
        self.tickers = []
        self.start = '01-01-2018'
        self.end = '01-01-2020'
        self.metaData = MetaData()
        self.plotting = Plotting(self.metaData)
        self.allocation = None

    def give_menu_of_options(self):
        options = ['1', '2', '3', '4']
        text = None
        print("\n\n     Hey Hey\n\n")
        text = input('Load csv Tickers or Add tickers [load/add]: (Default = load)')
        if text == '' or text == 'load':
            try:
                self.read_csv()
            except:
                print('could not find ../tickers/tickers.csv')
        else:
            self.ask_for_tickers()
        DataCollection.get(
                    self.tickers, 
                    start=self.start,
                    end=self.end
        )
        while text not in options:
            text = input('Choose from the following\n\
                1) Show Tickers\n\
                2) Portfolio Descriptive Statistics\n\
                3) Run Monte Carlo Simulation\n\n')
            if text == '1':
                self.show_tickers()
            elif text == '2':
                self.descriptive_stat_walkthrough()
            elif text == '3':
                self.monte_carlo_simulation()

    # Option 1
    def show_tickers(self):
        print("\n\n", self.tickers)

    # Option 2
    def ask_for_tickers(self):
        text = None        
        while text != "":
            text = input('\n\nEnter A Ticker or Hit Enter When Done\n')
            if text != '' and text != "":
                self.tickers.append(text.upper())
        print('Currently your tickers are: ')
        print(self.tickers)
        return self.tickers

    def read_csv(self):
        text = input('Would you like to read tickers.csv from the csv folder[yes/no]?: (Default: yes) ')
        if text == 'yes' or text == '':
            self.tickers = ReadCSV.get_tickers()

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
        metaData = MetaData()
        av_ret, pair_cov, correl = metaData.descriptive_statistics()
        print('\n---Average Return---\n\n', av_ret)
        print('\n\n---Pairwise Covariance---\n\n', pair_cov)
        print('\n\n---Correlation Matrix---\n\n', correl)

    # 3b - Plotting
    def plotting_walkthrough(self):
        self.plotting = Plotting()
        options = ['1', '2']
        text = None
        while text not in options:
            print('Not Working Yet')

    # 4 - Monte Carlo Simulation
    def monte_carlo_simulation(self):
        monte = MonteCarlo()
        while True:
            text = input('\n\nHow many Portfolios would you like to simulate? (Default = 15,000)\n\n')
            try:
                if text == '':
                    num_ports = 15000
                    break
                num_ports = int(text)
                break
            except:
                print('Please Enter Numbers Only')
            
        print('The simulation is now running.\n')
        monte.run_simulation(num_ports)
