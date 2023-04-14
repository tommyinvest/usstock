# Twelve Data
#
# Access 100,000+ symbols for stock, forex, index, and fundamental data from global markets.
# https://github.com/twelvedata/twelvedata-python
# https://twelvedata.com/
# https://twelvedata.com/account

from twelvedata import TDClient
import mplfinance

# Initialize client - apikey parameter is requiered
td = TDClient(apikey="99b5ae86072b40b69e66cebd2d67cfdb")

# Construct the necessary time series
ts = td.time_series(
    symbol="AAPL",
    interval="1min",
    outputsize=10,
    timezone="America/New_York",
)

# Returns pandas.DataFrame
print(ts.as_pandas())

# td = TDClient(apikey="YOUR_API_KEY_HERE")

# Get all expiration dates
expirations = td.get_options_expiration(
    symbol="AAPL",
).as_json()['dates']

# Extract only put options for the soonest expiration date
put_options = td.get_options_chain(
    symbol="AAPL",
    side="put",
    expiration_date=expirations[0]
).as_json()['puts']

print(put_options)

# ts = td.time_series(
#     symbol="MSFT",
#     outputsize=75,
#     interval="1day",
# )
#
# # 1. Returns OHLCV chart
# ts.as_pyplot_figure()
#
# # 2. Returns OHLCV + BBANDS(close, 20, 2, SMA) + %B(close, 20, 2 SMA) + STOCH(14, 3, 3, SMA, SMA)
# ts.with_bbands().with_percent_b().with_stoch(slow_k_period=3).as_pyplot_figure()

# ts = td.time_series(
#     symbol="MSFT",
#     outputsize=75,
#     interval="1day",
# )
#
# # 1. Returns OHLCV chart
# ts.as_pyplot_figure()
#
# # 2. Returns OHLCV + BBANDS(close, 20, 2, SMA) + %B(close, 20, 2 SMA) + STOCH(14, 3, 3, SMA, SMA)
# ts.with_bbands().with_percent_b().with_stoch(slow_k_period=3).as_pyplot_figure()
