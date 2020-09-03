class Display:

    def __init__(self):
        self.tickers = None
        self.start = None
        self.end = None

    def ask_for_tickers(self):
        tickers = []
        text = None
        while text != "Finish":
            text = input('Type Finish When Done\nEnter Stock Tickers\n')
            if text != '' and text != "Finish":
                tickers.append(text.upper())
        self.tickers = tickers
        return self.tickers

    def give_menu_of_options(self):
        options = ['1', '2', '3', '4']
        text = None
        print("Hey hey")
        while text not in options:
            text = input(
                'Choose from the following\n1) Portfolio Descriptive Statistics')
        return text


# d = Display()
# d.ask_for_tickers()
# print(d.tickers)
