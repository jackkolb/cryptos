import urllib.request
import json


class Liquid:

    def __init__(self):
        self.api_key = ""
        self.api_secret = ""

        self.buy_fee_baseline = 0.0
        self.buy_fee_percentage = .0035

        self.sell_fee_baseline = 0.0
        self.sell_fee_percentage = .0035

        self.withdraw_fee_baseline = 0.0  # unconfirmed
        self.withdraw_fee_percentage = 0.0  # unconfirmed

        self.deposit_fee_baseline = 0.0  # unconfirmed
        self.deposit_fee_percentage = 0.0  # unconfirmed

        self.can_buy = True
        self.can_sell = True

        self.coinwatch = ['ETH', 'BTC']

    def get_name(self):
        return "Liquid"

    def get_price(self):
        try:
            response = json.loads(urllib.request.urlopen(urllib.request.Request("https://api.liquid.com/products/27", headers={'User-Agent' : 'Magic Browser'})).read())
            price = (float(response["market_ask"]) + float(response["market_bid"])) / 2.0
        except Exception:
            price = "FAILED_LIQUID"
        return str(price)

    def get_bid(self):
        try:
            response = json.loads(urllib.request.urlopen(urllib.request.Request("https://api.liquid.com/products/27", headers={'User-Agent' : 'Magic Browser'})).read())
            price = response["market_bid"]
        except Exception:
            price = "FAILED_LIQUID"
        return str(price)

    def get_ask(self):
        try:
            response = json.loads(urllib.request.urlopen(urllib.request.Request("https://api.liquid.com/products/27", headers={'User-Agent' : 'Magic Browser'})).read())
            price = response["market_ask"]
        except Exception:
            price = "FAILED_LIQUID"
        return str(price)

    def buy(self):
        return True

    def sell(self):
        return True

    def transfer(self):
        return True
