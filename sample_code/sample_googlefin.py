# googlefinance
#
# Python module to get stock data from Google Finance API. This module provides no delay, real time stock data in NYSE & NASDAQ.
# https://github.com/hongtaocai/googlefinance
from googlefinance import getQuotes
# from googlefinance import getNews
import json
print(json.dumps(getQuotes('AAPL'), indent=2))
print(json.dumps(getQuotes(['AAPL', 'VIE:BKS']), indent=2))
# print(json.dumps(getNews("GOOG"), indent=2))
