# Alpha Vantage
#
# Alpha Vantage delivers a free API for real-time financial data and most used finance indicators in a simple JSON or CSV format.
# https://github.com/RomelTorres/alpha_vantage

API_KEY = 'R3QRCN30LDWC1EM7'
API_KEY = 'YOUR_API_KEY'


from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key=API_KEY)
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
print(data)
print(meta_data)

# ts = TimeSeries(key=API_KEY,rapidapi=True)

from pprint import pprint
ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(2))

from alpha_vantage.sectorperformance import SectorPerformances
import matplotlib.pyplot as plt

sp = SectorPerformances(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()

from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt

cc = CryptoCurrencies(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='CNY')
data['4b. close (USD)'].plot()
plt.tight_layout()
plt.title('Daily close value for bitcoin (BTC)')
plt.grid()
plt.show()
