import urllib.request
import json


class SIMEX:

    def __init__(self):
        self.api_key = ""

        self.buy_fee_baseline = 0
        self.buy_fee_percentage = .001

        self.sell_fee_baseline = 0
        self.sell_fee_percentage = .001

        self.withdraw_fee_baseline = .01  # unconfirmed
        self.withdraw_fee_percentage = 0  # unconfirmed

        self.deposit_fee_baseline = 0  # unconfirmed
        self.deposit_fee_percentage = 0  # unconfirmed

        self.coinwatch = ['ETH', 'BTC', 'LTC', 'USD']

        self.can_buy = True
        self.can_sell = True

    def get_name(self):
        return "SIMEX"

    def get_price(self):
        price = -1
        try:
            response = json.loads(urllib.request.urlopen("https://simex.global/api/pairs").read().decode('utf-8'))
            for pair in response["data"]:
                if pair["name"] == "ETH_USD":
                    price = (float(pair["buy_price"]) + float(pair["sell_price"])) / 2.0  # returns average of buy/sell
                    break
        except Exception:
            print("Failed SIMEX")
        return str(price)

    def get_bid(self):
        price = -1
        try:
            response = json.loads(urllib.request.urlopen("https://simex.global/api/pairs").read().decode('utf-8'))
            for pair in response["data"]:
                if pair["name"] == "ETH_USD":
                    price = pair["buy_price"]
                    break
        except Exception:
            print("Failed SIMEX")
        return str(price)

    def get_ask(self):
        price = -1
        try:
            response = json.loads(urllib.request.urlopen("https://simex.global/api/pairs").read().decode('utf-8'))
            for pair in response["data"]:
                if pair["name"] == "ETH_USD":
                    price = pair["sell_price"]
                    break
        except Exception:
            print("Failed SIMEX")
        return str(price)

    def buy(self):
        return True

    def sell(self):
        return True

    def transfer(self):
        return True
