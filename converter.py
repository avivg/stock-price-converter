import urllib.request
import json

API_KEY = open('converter_key.txt').readlines()[0]

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
        return 'http://free.currencyconverterapi.com/api/v5/convert?q=%s&compact=y&apiKey=%s' % (self._conversion_name(), API_KEY)

    def _conversion_name(self):
        return '{f}_{t}'.format(f=self._from, t=self._to)

    def _get_online_exchange_rate(self, url):
        contents = urllib.request.urlopen(url).read()
        val = json.loads(contents.decode())
        val = val[self._conversion_name()]['val']
        return float(val)
