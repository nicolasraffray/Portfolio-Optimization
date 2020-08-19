class Display:

    def __init__(self):
        self.tickers = None
        pass

    def ask_for_tickers(self):
        tickers = []
        text = None
        while text != "":
            text = input('Enter Stock Tickers\n')
            if text != '':
                tickers.append(text.upper())
        self.tickers = tickers
        return self.tickers


# d = Display()
# d.ask_for_tickers()
# print(d.tickers)
