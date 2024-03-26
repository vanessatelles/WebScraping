import aiohttp
import asyncio
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

async def fetch_data_from_api(url):

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

    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    response = await fetch_data_from_api(url)
    # parse data from the html into a beautifulsoup object
    soup = BeautifulSoup(response, 'html.parser')
    companies_table=soup.find('table',{'id':'constituents','class':"wikitable sortable"})
    a = companies_table.find_all('a',{'class':"external text"})
    symbols =  [symbol.text.strip() for symbol in a[:50]]        

    return symbols

async def previous_close(symbols):

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

if __name__ == '__main__':
    print("start")