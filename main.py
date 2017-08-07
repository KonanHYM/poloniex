import json

from config.config import APIKEY
from module.poloniex import Poloniex


if __name__ == '__main__':
    apikey = APIKEY['APIKey']
    secret = APIKEY['Secret']
    poloniex = Poloniex(apikey, secret)
    query_json = poloniex.api_query('returnTicker')
    print 'ETH ' + json.dumps(query_json['USDT_ETH']['last'], indent=4)
    print 'XRP ' + json.dumps(query_json['USDT_XRP']['last'], indent=4)
    print 'BTC ' + json.dumps(query_json['USDT_BTC']['last'], indent=4)

    my_balance = poloniex.returnMarketTradeHistory('USDT_ETH')
    print json.dumps(my_balance, indent=4)
