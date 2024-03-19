import urllib.request
import json


class Binance:

    def __init__(self):
        self.api_key = ""
        self.api_secret = ""

        self.buy_fee_baseline = 0
        self.buy_fee_percentage = .001

        self.sell_fee_baseline = 0
        self.sell_fee_percentage = .001

        self.withdraw_fee_baseline = .01  # confirmed
        self.withdraw_fee_percentage = 0  # confirmed

        self.deposit_fee_baseline = 0  # confirmed 0
        self.deposit_fee_percentage = 0  # confirmed 0

        self.coinwatch = ['ETH', 'BTC', 'LTC', 'USD']

        self.can_buy = False
        self.can_sell = False

    def get_name(self):
        return "Binance"

    def get_price(self):
        price = -1
        try:
            response = json.loads(urllib.request.urlopen("https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT").read().decode('utf-8'))
            price = response["price"]
        except Exception:
            print("[FAILED] Binance")
        return str(price)

    def get_ask(self):
        price = -1
        try:
            response = json.loads(
                urllib.request.urlopen("https://api.binance.com/api/v3/ticker/bookTicker?symbol=ETHUSDT").read().decode('utf-8'))
            price = response["askPrice"]
        except Exception:
            print("[FAILED] Binance")
        return str(price)

    def get_bid(self):
        price = -1
        try:
            response = json.loads(
                urllib.request.urlopen("https://api.binance.com/api/v3/ticker/bookTicker?symbol=ETHUSDT").read().decode('utf-8'))
            price = response["bidPrice"]
        except Exception:
            print("[FAILED] Binance")
        return str(price)

    def buy(self):
        return True

    def sell(self):
        return True

    def transfer(self):
        return True
