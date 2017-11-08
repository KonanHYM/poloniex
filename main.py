# coding:utf-8 = =#
import json
import numpy

from scipy import stats
from scipy.stats import norm

from config.config import APIKEY
from module.poloniex import Poloniex

def statics():
    a = numpy.array([2.9, 4.7, 6.3, 3.0, 7.0, 3.5])
    print numpy.std(a)  #标准差
    print numpy.std(a, ddof=1)  #样本标准差
    print numpy.var(a)  #方差
    print numpy.cov(a)  #样本方差
    print numpy.mean(a) #平均值

def det():
    a = numpy.array([
        [1,2,3],
        [4,7,8],
        [9,10,1]
    ])
    b = numpy.array(
        [0, 8, -9]
        )
    print numpy.linalg.det(a)   #求取行列式
    print numpy.linalg.inv(a)   #求取逆矩阵
    print numpy.linalg.solve(a,b)   #求取方程组的解
    x = numpy.linalg.solve(a, b)
    print numpy.dot(a, x)   #求取矩阵的乘积

if __name__ == '__main__':
    det()
    # apikey = APIKEY['APIKey']
    # secret = APIKEY['Secret']
    # poloniex = Poloniex(apikey, secret)
    # query_json = poloniex.api_query('returnTicker')
    # print 'ETH ' + json.dumps(query_json['USDT_ETH']['last'], indent=4)
    # print 'XRP ' + json.dumps(query_json['USDT_XRP']['last'], indent=4)
    # print 'BTC ' + json.dumps(query_json['USDT_BTC']['last'], indent=4)
    #
    # my_balance = poloniex.returnMarketTradeHistory('USDT_ETH')
    # print json.dumps(my_balance, indent=4)
