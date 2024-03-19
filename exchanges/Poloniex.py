import urllib
import urllib.request
import urllib.parse
import json
import time
import hmac
import hashlib


class Poloniex:
    def __init__(self):
        self.APIKey = ""
        self.Secret = ""

        self.buy_fee_baseline = 0
        self.buy_fee_percentage = .002

        self.sell_fee_baseline = 0
        self.sell_fee_percentage = .002

        self.withdraw_fee_baseline = .01
        self.withdraw_fee_percentage = 0  # confirmed 0

        self.withdraw_fee_usd_baseline = 10  # confirmed

        self.deposit_fee_baseline = 0
        self.deposit_fee_percentage = 0

        self.can_buy = True
        self.can_sell = True

    def get_name(self):
        return "Poloniex"

    def get_price(self):
        try:
            tickers = self.returnTicker()
            price = tickers['USDT_ETH']['last']
        except KeyboardInterrupt:
            price = "FAILED_POLONIEX"
        return str(price)

    def get_bid(self):
        try:
            tickers = self.returnTicker()
            price = tickers['USDT_ETH']['highestBid']
        except KeyboardInterrupt:
            price = "FAILED_POLONIEX"
        return str(price)

    def get_ask(self):
        try:
            tickers = self.returnTicker()
            price = tickers['USDT_ETH']['lowestAsk']
        except KeyboardInterrupt:
            price = "FAILED_POLONIEX"
        return str(price)

    def createTimeStamp(self, datestr, format="%Y-%m-%d %H:%M:%S"):
        return time.mktime(time.strptime(datestr, format))

    def post_process(self, before):
        after = before

        # Add timestamps if there isnt one but is a datetime
        if ('return' in after):
            if (isinstance(after['return'], list)):
                for x in range(0, len(after['return'])):
                    if (isinstance(after['return'][x], dict)):
                        if ('datetime' in after['return'][x] and 'timestamp' not in after['return'][x]):
                            after['return'][x]['timestamp'] = float(self.createTimeStamp(after['return'][x]['datetime']))

        return after

    def api_query(self, command, req={}):
        req['command'] = command
        req['nonce'] = int(time.time() * 1000)
        post_data = urllib.parse.urlencode(req)

        sign = hmac.new(self.Secret, post_data, hashlib.sha512).hexdigest()
        headers = {
            'Sign': sign,
            'Key': self.APIKey
        }

        ret = urllib.request.urlopen(urllib.request.Request('https://poloniex.com/tradingApi', post_data, headers))
        jsonRet = json.loads(ret.read())
        return self.post_process(jsonRet)

    def returnTicker(self):
        ret = urllib.request.urlopen(urllib.request.Request('https://poloniex.com/public?command=' + "returnTicker"))
        return json.loads(ret.read())

    def returnOpenOrders(self, currencyPair):
        return self.api_query('returnOpenOrders', {"currencyPair": currencyPair})

    def buy(self, currencyPair, rate, amount):
        return self.api_query('buy', {"currencyPair": currencyPair, "rate": rate, "amount": amount})

    def sell(self, currencyPair, rate, amount):
        return self.api_query('sell', {"currencyPair": currencyPair, "rate": rate, "amount": amount})

    def cancel(self, currencyPair, orderNumber):
        return self.api_query('cancelOrder', {"currencyPair": currencyPair, "orderNumber": orderNumber})

    def withdraw(self, currency, amount, address):
        return self.api_query('withdraw', {"currency": currency, "amount": amount, "address": address})
