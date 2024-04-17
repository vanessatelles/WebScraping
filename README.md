# Web Scraping a Wikipedia table

This project performs web scraping to collect financial information about companies in the S&P 500 index. The goal is to identify which companies have a previous closing price below their 200-day moving average. Here's an overview of the process:

- **Data Collection from Wikipedia**:
  The first step is to scrape a table from Wikipedia with a list of companies in the S&P 500 index. The link used for this is:
  [List of S&amp;P 500 Companies on Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)
- **Select the First 50 Ticker Symbols**:
  After extracting the table, we save the symbols (ticker symbols) of 50 companies for further operations.
- **Fetch Previous Close Value**:
  For each of the 50 ticker symbols, we use the following URL to retrieve the previous close value:
  [Yahoo Finance](https://finance.yahoo.com/quote/AAPL?p=AAPLtsrc=fin-srch)
- **Store Data in a Pandas DataFrame**:
  The previous close values are stored along with their corresponding ticker symbols in a Pandas DataFrame.
- **Fetch 200-Day Moving Average Value**:
  For each company symbol, we use another URL to obtain the 200-day moving average:
  [Yahoo Finance - Key Statistics](https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL)
- **Add Data to the DataFrame**:
  The 200-day moving average values are added to the same DataFrame.
