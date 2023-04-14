# Wallstreet
#
# Wallstreet is a Python 3 library for monitoring and analyzing real time Stock and Option data. Quotes are provided from the Google Finance API.
# https://github.com/mcdallas/wallstreet
from wallstreet import Stock, Call, Put
import pandas as pd

s = Stock('AAPL')
print(s.price)
print(s.change)
print(s.last_trade)

# g = Call('GOOG', d=12, m=2, y=2023, strike=700)
# print(g.price)
# print(g.implied_volatility())
# print(g.delta())
# print(g.vega())
# print(g.underlying.price)

s = Stock('BTC-USD')
df = s.historical(days_back=30, frequency='d')
print(df)
