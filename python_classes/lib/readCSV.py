import csv

class ReadCSV:

  @staticmethod
  def get_tickers(path_and_filename=None):
    if path_and_filename == None:
      path_and_filename = 'tickers/tickers.csv'
    with open(path_and_filename, newline='') as f:
      reader = csv.reader(f)
      data = [row[0] for row in reader]
      return data
