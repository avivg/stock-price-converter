class Quoter(object):
    def __init__(self, stock_price_getter=None, exchange_rate_getter=None):
        self._init_price(stock_price_getter)
        self._init_exchange_rate(exchange_rate_getter)

    def _init_price(self, stock_price_getter):
        if stock_price_getter is not None:
            self._stock_price = stock_price_getter.get_stock_price()
        else:
            self._stock_price = 0

    def _init_exchange_rate(self, getter):
        if getter is not None:
            self._exchange_rate = getter.get_exchange_rate()
        else:
            self._exchange_rate = 1

    def get_usd_price(self):
        return self._stock_price

    def get_exchange_rate(self):
        return self._exchange_rate

    def get_converted_price(self):
        return self._stock_price * self._exchange_rate

    def __str__(self):
        return str(self.get_converted_price())

