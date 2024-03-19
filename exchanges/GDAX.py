import urllib.request
import json


class GDAX:

    def __init__(self):
        self.gdax_api_pass = ""
        self.gdax_api_key = ""
        self.gdax_api_secret = ""

        self.buy_fee_baseline = 0
        self.buy_fee_percentage = .0025

        self.sell_fee_baseline = 0
        self.sell_fee_percentage = .0025

        self.withdraw_fee_baseline = 0  # confirm 0
        self.withdraw_fee_percentage = 0  # confirm 0

        self.withdraw_fee_usd_baseline = 0  # using ACH

        self.deposit_fee_baseline = 0  # confirmed
        self.deposit_fee_percentage = 0  # confirmed

        self.deposit_fee_usd_baseline = 0  # using ACH

        self.gdax_coinwatch = ['ETH', 'BTC', 'LTC', 'USD']

        self.can_buy = True
        self.can_sell = True

    def get_name(self):
        return "GDAX"

    def get_price(self):
        info_link = "https://api.gdax.com/products/ETH-USD/ticker"

        try:
            response = urllib.request.urlopen(info_link)
            data = json.loads(response.read().decode())
            price = data['price']
        except Exception:
            price = "FAILED_GDAX"

        return str(price)

    def get_bid(self):
        info_link = "https://api.gdax.com/products/ETH-USD/ticker"

        try:
            response = urllib.request.urlopen(info_link)
            data = json.loads(response.read().decode())
            price = data['bid']
        except Exception:
            price = "FAILED_GDAX"

        return str(price)

    def get_ask(self):
        info_link = "https://api.gdax.com/products/ETH-USD/ticker"

        try:
            response = urllib.request.urlopen(info_link)
            data = json.loads(response.read().decode())
            price = data['ask']
        except Exception:
            price = "FAILED_GDAX"

        return str(price)

    def buy(self):
        return True

    def sell(self):
        return True

    def transfer(self):
        return True
