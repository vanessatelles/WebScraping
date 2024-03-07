import requests

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

if __name__ == '__main__':
    
    print("start")