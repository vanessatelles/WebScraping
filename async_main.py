import aiohttp
import asyncio
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

async def fetch_data_from_api(url):
    """
    Async function to call the API and fetch data from the endpoint.
    It raises an except if time out.   

    Returns:
        response(text): Data received from the API.
    """
    conn = aiohttp.TCPConnector(limit=50)  # allows 50 concurrent connections
    timeout = aiohttp.ClientTimeout(total=20)  # timeout duration 
    
    async with aiohttp.ClientSession(connector= conn, timeout= timeout) as session:
        try:
            async with session.get(url, headers= HEADERS) as resp:
                response = await resp.text()
                return response 
        except asyncio.TimeoutError:
            # Handle a timeout error here
            print("Request timed out.")

async def get_symbols():
    """
    Async function to parse data from the html into a beautifulsoup object.
    Scrap the content for the stock symbols. 

    Returns:
        symbols(list): A list of the first 50 symbols in the S&P 500 companies table.
    """
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    response = await fetch_data_from_api(url)
    # parse data from the html into a beautifulsoup object
    soup = BeautifulSoup(response, 'html.parser')
    companies_table=soup.find('table',{'id':'constituents','class':"wikitable sortable"})
    a = companies_table.find_all('a',{'class':"external text"})
    symbols =  [symbol.text.strip() for symbol in a[:50]]        

    return symbols

async def previous_close(symbols):
    """
    Async function to feacth data from the API to each symbol.
    Parse data from html into a beautifulsoup object.
    Scrap the content for the Stock Previous Close Value;

    Returns:
        previous_close_values(list): A list with the previous close value to each stock.
    """
    previous_close_values = []
    for symbol in symbols:
        url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}tsrc=fin-srch'
        response = await fetch_data_from_api(url)
        page  = BeautifulSoup(response, 'html.parser')
        previous_close_value = page.find('td', {'data-test':"PREV_CLOSE-value"})
        previous_close_values.append(float(previous_close_value.text))
        #print(f"P: {previous_close_value.text}")
    print("Got all previous close values.")
    return previous_close_values

async def moving_average(symbols):
    """
    Async function to feacth data from the API to each symbol.
    Parse data from html into a beautifulsoup object.
    Scrap the content for the Stock 200-Day Moving Average value.

    Returns:
        moving_average_values(list): A list with the moving average value to each stock.
    """
    moving_average_values = []

    for symbol in symbols:
        url = f'https://finance.yahoo.com/quote/{symbol}/key-statistics?p={symbol}'
        response = await fetch_data_from_api(url)
        page  = BeautifulSoup(response, 'html.parser')
        two_columns = page.find('div',{'id':'Col1-0-KeyStatistics-Proxy'})
        right_column = two_columns.find('div', {'class':'Fl(end) W(50%) smartphone_W(100%)'})
        td = right_column.find_all('td',{'class':'Fw(500) Ta(end) Pstart(10px) Miw(60px)'})
        moving_average_value = td[6]
        #print(f"M: {moving_average_value.text}")
        moving_average_values.append(float(moving_average_value.text))
    print("Got all moving average values.")
    return moving_average_values

async def get_stock_value():

    ticker_values = await get_symbols()
    print("Got all tickers.")
    previous_close_values, moving_average_values = await asyncio.gather(previous_close(ticker_values), moving_average(ticker_values))
    return ticker_values, previous_close_values, moving_average_values

if __name__ == '__main__':
    stock_values = asyncio.run(get_stock_value())