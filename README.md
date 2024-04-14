# WebScraping


1. Scrape the S&P 500 companies table from the following Wikipedia page:
   - https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
1. Save the companies ticker symbols into a list. Cut the list to take only the first 50 elements.
1. For each ticker symbol in the list, call the following API In order to get the Previous Close value for each company:
   - https://finance.yahoo.com/quote/AAPL?p=AAPLtsrc=fin-srch
1. Save this value and the ticker symbol in a Pandas dataframe.
1. For each ticker symbol also call the following API endpoint in order to get the 200-Day Moving Average value:
   - https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL
1. Save this value in a new column of the same dataframe.
1. Compute a new column in the dataframe called “is_cheap”with a Boolean value which is ``True`` if the Previous Close is
   lower than the 200-Day Moving Average and ``False`` otherwise.
1. Concatenate all dataframes for all ticker symbols in one.
1. Display the dataframe on a plot only for the companies where ``is_cheap = True.``
1. On the X axis should be the Ticker symbol and on the Y axis the Previous Close value.

## To-do
- Rewrite README
- Separate into files
- Write a post about
- Add requirements
