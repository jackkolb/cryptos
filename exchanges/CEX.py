import urllib.request
import json


class CEX:

    def __init__(self):
        self.user_id = ""
        self.api_key = ""
        self.api_secret = ""

        self.buy_fee_baseline = 0
        self.buy_fee_percentage = .0025

        self.sell_fee_baseline = 0
        self.sell_fee_percentage = .0025

        self.withdraw_fee_baseline = .00  #
        self.withdraw_fee_percentage = 0  #

        self.deposit_fee_baseline = 0  #
        self.deposit_fee_percentage = 0  #

        self.coinwatch = ['ETH', 'BTC', 'LTC', 'USD']

        self.can_buy = True
        self.can_sell = False # international, expensive to xfer

    def get_name(self):
        return "CEX"

    def get_price(self): # not done yet!!
        price = -1
        try:
            response = json.loads(urllib.request.urlopen(urllib.request.Request("https://cex.io/api/ticker/ETH/USD", headers={'User-Agent' : 'Magic Browser'})).read())
            price = response["last"]
        except KeyboardInterrupt:
            print("[FAILED] CEX")
        return str(price)

    def get_ask(self):
        price = -1
        try:
            response = json.loads(urllib.request.urlopen(urllib.request.Request("https://cex.io/api/ticker/ETH/USD", headers={'User-Agent' : 'Magic Browser'})).read())
            price = response["ask"]
        except KeyboardInterrupt:
            print("[FAILED] CEX")
        return str(price)

    def get_bid(self):
        price = -1
        try:
            response = json.loads(urllib.request.urlopen(urllib.request.Request("https://cex.io/api/ticker/ETH/USD", headers={'User-Agent' : 'Magic Browser'})).read())
            price = response["bid"]
        except KeyboardInterrupt:
            print("[FAILED] CEX")
        return str(price)

    def buy(self):
        return True

    def sell(self):
        return True

    def transfer(self):
        return True
