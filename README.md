# Web Scraping a Wikipedia table

This project performs web scraping to collect financial information about companies in the S&P 500 index. The goal is to identify which companies have a previous closing price below their 200-day moving average. Two versions of the code were implemented: one synchronous and one asynchronous.

## Synchronous and Asynchronous Code

Two versions of the code were created for this project: a synchronous version and an asynchronous version. The synchronous code executes tasks sequentially, while the asynchronous code can perform multiple tasks simultaneously, improving efficiency when dealing with numerous network requests.

The asynchronous code is ideal for high-latency operations, such as multiple HTTP requests, allowing concurrent execution to reduce waiting times. This is especially useful when scraping large datasets or multiple endpoints. However, synchronous code is often simpler and easier to understand, which might be helpful for smaller datasets or simpler use cases.

## Overview of the process:

- **Data Collection from Wikipedia**:
  The first step involves scraping a table from Wikipedia with a list of companies in the S&P 500 index. The link used for this is:
  [List of S&amp;P 500 Companies on Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)
- **Select the First 50 Ticker Symbols**:
  After extracting the table, we save the symbols (ticker symbols) of 50 companies for further operations.
- **Fetch Previous Close Value**:
  For each of the 50 ticker symbols, the following URL is used to retrieve the previous close value:
  [Yahoo Finance](https://finance.yahoo.com/quote/AAPL?p=AAPLtsrc=fin-srch)
- **Store Data in a Pandas DataFrame**:
  The previous close values are stored along with their corresponding ticker symbols in a Pandas DataFrame.
- **Fetch 200-Day Moving Average Value**:
  For each company symbol, another URL is used to obtain the 200-day moving average:
  [Yahoo Finance - Key Statistics](https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL)
- **Add Data to the DataFrame**:
  The 200-day moving average values are added to the same DataFrame.
- **Compute an "is_cheap" Column**:
  A new column called "is_cheap" is created to indicate whether the previous close is lower than the 200-day moving average. If it's lower, the value is `True`; otherwise, it's `False`.
- **Concatenate DataFrames and Visualize Data**:
  All individual DataFrames are concatenated into a single DataFrame. A plot is then created for the companies where "is_cheap" is `True`. The X-axis represents the ticker symbols, and the Y-axis represents the previous close value.

This process quickly identifies the companies in the S&P 500 that may be considered "cheap" relative to their 200-day moving average. The result is a visually intuitive plot showing these companies, helping with financial analysis or investment decision-making.
<div align="center"> 
  
![plot](https://github.com/vanessatelles/WebScraping/assets/15792134/bb2bc123-f156-40d4-93fb-5359e343d427)

</div> 
