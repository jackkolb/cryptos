import urllib.request
import json


class itBit:

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
        return "itBit"

    def get_price(self):
        try:
            response = json.loads(urllib.request.urlopen("https://api.itbit.com/v1/markets/ETHUSD/ticker").read().decode('utf-8'))
            price = (float(response["bid"]) + float(response["ask"])) / 2.0
        except Exception:
            price = "FAILED_ITBIT"
        return str(price)

    def get_bid(self):
        try:
            response = json.loads(urllib.request.urlopen("https://api.itbit.com/v1/markets/ETHUSD/ticker").read().decode('utf-8'))
            price = float(response["bid"])
        except Exception:
            price = "FAILED_ITBIT_BID"
        return str(price)

    def get_ask(self):
        try:
            response = json.loads(urllib.request.urlopen("https://api.itbit.com/v1/markets/ETHUSD/ticker").read().decode('utf-8'))
            price = float(response["ask"])
        except Exception:
            price = "FAILED_ITBIT_ASK"
        return str(price)

    def buy(self):
        return True

    def sell(self):
        return True

    def transfer(self):
        return True
