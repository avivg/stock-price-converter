import urllib2
import json

class CurrencyConverter(object):
    def __init__(self, fr='USD', to='ILS'):
        self._from = fr
        self._to = to

    def get_exchange_rate(self):
        return self._request_exchange_rate()

    def _request_exchange_rate(self):
        url = self._request_url()
        return self._get_online_exchange_rate(url)

    def _request_url(self):
        return 'http://free.currencyconverterapi.com/api/v5/convert?q=%s&compact=y' % (self._conversion_name())

    def _conversion_name(self):
        return '{f}_{t}'.format(f=self._from, t=self._to)

    def _get_online_exchange_rate(self, url):
        contents = urllib2.urlopen(url)
        val = json.load(contents)
        val = val[self._conversion_name()]['val']
        return float(val)
