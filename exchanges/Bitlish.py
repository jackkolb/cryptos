import urllib.request
import json


class Bitlish:

    def __init__(self):
        self.api_key = ""
        self.api_secret = ""

        self.buy_fee_baseline = 0
        self.buy_fee_percentage = .003

        self.sell_fee_baseline = 0
        self.sell_fee_percentage = .003

        self.withdraw_fee_baseline = .01
        self.withdraw_fee_percentage = 0

        self.deposit_fee_baseline = 10  # confirmed 0
        self.deposit_fee_percentage = 0  # confirmed 0

        self.coinwatch = ['ETH', 'BTC', 'LTC', 'XMR', 'USD']

        self.can_buy = True
        self.can_sell = False

    def get_name(self):
        return "Bitlish"

    def get_price(self):
        price = -1
        try:
            response = json.loads(urllib.request.urlopen("https://bitlish.com/api/v1/tickers").read().decode('utf-8'))
            price = response["ethusd"]["last"]
        except Exception:
            print("[FAILED] Bitlish")
        return str(price)

    def get_ask(self):
        price = -1
        try:
            response = json.loads(urllib.request.urlopen("https://bitlish.com/api/v1/tickers").read().decode('utf-8'))
            price = response["ethusd"]["ask"]
        except Exception:
            print("[FAILED] Bitlish")
        return str(price)

    def get_bid(self):
        price = -1
        try:
            response = json.loads(urllib.request.urlopen("https://bitlish.com/api/v1/tickers").read().decode('utf-8'))
            price = response["ethusd"]["bid"]
        except Exception:
            print("[FAILED] Bitlish")
        return str(price)

    def buy(self):
        return True

    def sell(self):
        return True

    def transfer(self):
        return True
