# from lib.dataCollection import DataCollection
from lib.display import Display
from lib.metaData import MetaData
from lib.plotting import Plotting
from lib.monteCarlo import MonteCarlo

def main():
    display = Display()
    print('\n\n========= Tickers =========\n\n')
    display.initial_data_request()
    while True:
        display.give_menu_of_options()

if __name__ == "__main__":
    main()
    
