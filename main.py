# from lib.dataCollection import DataCollection
from python_classes.lib.display import Display
from python_classes.lib.metaData import MetaData
from python_classes.lib.plotting import Plotting
from python_classes.lib.monteCarlo import MonteCarlo

def main():
    display = Display()
    while True:
        display.give_menu_of_options()

if __name__ == "__main__":
    main()
    
