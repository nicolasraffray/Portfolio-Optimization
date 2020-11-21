# from lib.dataCollection import DataCollection
from lib.display import Display
from lib.metaData import MetaData
from lib.plotting import Plotting

if __name__ == "__main__":
    display = Display()
    while True:
        display.give_menu_of_options()
