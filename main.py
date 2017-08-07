import json

from config.config import APIKEY
from module.poloniex import Poloniex


if __name__ == '__main__':
    apikey = APIKEY['APIKey']
    secret = APIKEY['Secret']
    poloniex = Poloniex(apikey, secret)
    query_json = poloniex.api_query('returnTicker')
    print json.dumps(query_json['USDT_BTC'], indent=4)
