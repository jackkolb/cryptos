import urllib.request
import json


class Bitstamp:

    def __init__(self):
        self.api_key = ""
        self.api_secret = ""

        self.buy_fee_baseline = 0
        self.buy_fee_percentage = .0025

        self.sell_fee_baseline = 0
        self.sell_fee_percentage = .0025

        self.withdraw_fee_baseline = .00  # confirmed 0
        self.withdraw_fee_percentage = 0  # confirmed 0

        self.deposit_fee_baseline = 0  # confirmed 0
        self.deposit_fee_percentage = 0  # confirmed 0

        self.coinwatch = ['ETH', 'BTC', 'LTC', 'XMR', 'USD']

        self.can_buy = True
        self.can_sell = False # international, expensive to xfer

    def get_name(self):
        return "Bitstamp"

    def get_price(self):
        price = -1
        try:
            response = json.loads(urllib.request.urlopen("https://www.bitstamp.net/api/v2/ticker/ethusd/").read().decode('utf-8'))
            price = response["last"]
        except Exception:
            print("[FAILED] Bitstamp")
        return str(price)

    def get_ask(self):
        price = -1
        try:
            response = json.loads(urllib.request.urlopen("https://www.bitstamp.net/api/v2/ticker/ethusd/").read().decode('utf-8'))
            price = response["ask"]
        except Exception:
            print("[FAILED] Bitstamp")
        return str(price)

    def get_bid(self):
        price = -1
        try:
            response = json.loads(urllib.request.urlopen("https://www.bitstamp.net/api/v2/ticker/ethusd/").read().decode('utf-8'))
            price = response["bid"]
        except Exception:
            print("[FAILED] Bitstamp")
        return str(price)

    def buy(self):
        return True

    def sell(self):
        return True

    def transfer(self):
        return True
