import urllib2

class StockPriceGetter(object):
    def __init__(self, ticker):
        self._tick = ticker

    def get_stock_price(self):
        return self._request_stock_price()

    def _request_stock_price(self):
        url = self._generate_request_url()
        return self._get_online_stock_price(url)

    def _generate_request_url(self):
        return 'https://api.iextrading.com/1.0/stock/%s/price' % self._tick

    def _get_online_stock_price(self, url):
        contents = urllib2.urlopen(url).read()
        return float(contents)

