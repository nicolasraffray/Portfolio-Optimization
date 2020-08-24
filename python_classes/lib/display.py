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


# d = Display()
# d.ask_for_tickers()
# print(d.tickers)
