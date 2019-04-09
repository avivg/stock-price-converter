#!/usr/bin/python

from quoter import Quoter
from stock import StockPriceGetter
from converter import CurrencyConverter

if __name__ == '__main__':
    stock = StockPriceGetter('AVGO')
    exchange = CurrencyConverter(fr='USD', to='ILS')
    qtr = Quoter(stock, exchange)
    print 'AVGO: ILS %6.2f' % qtr.get_converted_price()
