import aiohttp
import asyncio

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

if __name__ == '__main__':
    print("start")