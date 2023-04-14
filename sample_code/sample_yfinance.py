# yfinance
#
# Data for stocks (historic, intraday, fundamental), FX, crypto, and options. Uses Yahoo Finance so any data available through Yahoo is available through yfinance.
# https://github.com/ranaroussi/yfinance
import yfinance as yf

df = yf.download(tickers = "SPY AAPL",  # list of tickers
            period = "1y",         # time period
            interval = "1d",       # trading interval
            prepost = False,       # download pre/post market hours data?
            repair = True)         # repair obvious price errors e.g. 100x?
print(df)
# msft = yf.Ticker("MSFT")
#
# # get all stock info
# print(msft.info)
#
# # get historical market data
# hist = msft.history(period="1mo")
# print(hist)
# # show meta information about the history (requires history() to be called first)
# print(msft.history_metadata)
#
# # show actions (dividends, splits, capital gains)
# print(msft.actions)
# print(msft.dividends)
# print(msft.splits)
# print(msft.capital_gains)  # only for mutual funds & etfs
#
# # show share count
# # - yearly summary:
# msft.shares
# # - accurate time-series count:
# msft.get_shares_full(start="2022-01-01", end=None)
#
# # show financials:
# # - income statement
# msft.income_stmt
# msft.quarterly_income_stmt
# # - balance sheet
# msft.balance_sheet
# msft.quarterly_balance_sheet
# # - cash flow statement
# msft.cashflow
# msft.quarterly_cashflow
# # see `Ticker.get_income_stmt()` for more options
#
# # show holders
# msft.major_holders
# msft.institutional_holders
# msft.mutualfund_holders
#
# # show earnings
# msft.earnings
# msft.quarterly_earnings
#
# # show sustainability
# msft.sustainability
#
# # show analysts recommendations
# msft.recommendations
# msft.recommendations_summary
# # show analysts other work
# msft.analyst_price_target
# msft.revenue_forecasts
# msft.earnings_forecasts
# msft.earnings_trend
#
# # show next event (earnings, etc)
# msft.calendar
#
# # Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default.
# # Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
# msft.earnings_dates
#
# # show ISIN code - *experimental*
# # ISIN = International Securities Identification Number
# msft.isin
#
# # show options expirations
# msft.options
#
# # show news
# msft.news
#
# # get option chain for specific expiration
# opt = msft.option_chain('YYYY-MM-DD')
# # data available via: opt.calls, opt.puts
