import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


def fetch_data_from_api(url):
  """
  Method to call the API and fetch data from the endpoint.    
  Returns:
      dict: Data received from the API as a JSON dictionary.
  """
  try:
    response = requests.get(url, headers= HEADERS, timeout= 20)
    return response.text
  except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")   

def get_symbols():
  """
    Parse data from the html into a beautifulsoup object.
    Scrap the content for the stock symbols. 
    Returns:
        symbols(list): A list of the first 50 symbols in the S&P 500 companies table.
    """
  response = fetch_data_from_api("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
  soup = BeautifulSoup(response, 'html.parser')
  companies_table=soup.find('table',{'id':'constituents','class':"wikitable sortable"})
  a = companies_table.find_all('a',{'class':"external text"})
  symbols = [symbol.text.strip() for symbol in a[:50]]

  print("Got all tickers.")

  return symbols


def get_previous_closeValue(symbols):
  """
  Feacth data from the API to each symbol.
  Parse data from html into a beautifulsoup object.
  Scrap the content for the Stock Previous Close Value;
  Returns:
    previous_close_values(list): A list with the previous close value to each stock.
  """
  previous_close_values = [] 
  
  for symbol in symbols:
    response = fetch_data_from_api(f'https://finance.yahoo.com/quote/{symbol}?p={symbol}tsrc=fin-srch')    
    page  = BeautifulSoup(response, 'html.parser')
    previous_close_value = page.find('td', {'data-test':"PREV_CLOSE-value"})
    previous_close_values.append(float(previous_close_value.text))

  print("Got all previous close values.")

  return previous_close_values

if __name__ == '__main__':

    ticker_values = get_symbols()
    previous_close_values = get_previous_closeValue(ticker_values)
