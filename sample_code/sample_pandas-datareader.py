# pandas-datareader
#
# pandas-datareader used to be part of the pandas project. Now an independent project. Includes data for stocks, FX, economic indicators, Fama-French factors, and many others.
# https://pandas-datareader.readthedocs.io/en/latest/
# pip install pandas-datareader
import pandas_datareader as pdr
print(pdr.get_data_fred('GS10'))
