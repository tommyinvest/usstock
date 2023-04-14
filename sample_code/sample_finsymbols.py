# finsymbols
#
# Obtains stock symbols and relating information for SP500, AMEX, NYSE, and NASDAQ.
# https://github.com/skillachie/finsymbols
# http://skillachie.github.io/finsymbols/

from finsymbols import symbols
sp500 = symbols.get_sp500_symbols()
print(sp500)
