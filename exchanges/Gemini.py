import urllib.request
import json

class Gemini:

    def __init__(self):
        self.api_key = ""
        self.api_secret = ""

        self.buy_fee_baseline = 0
        self.buy_fee_percentage = .0035

        self.sell_fee_baseline = 0
        self.sell_fee_percentage = .0035

        self.withdraw_fee_baseline = 0  # confirmed 0 for eth (unless > 10 per calendar month!!), 0 for USD always
        self.withdraw_fee_percentage = 0  # confirmed 0

        self.deposit_fee_baseline = 0  # confirmed 0
        self.deposit_fee_percentage = 0  # confirmed 0

        self.coinwatch = ['ETH', 'BTC', 'LTC', 'USD']

        self.can_buy = True
        self.can_sell = True

    def get_name(self):
        return "Gemini"

    def get_price(self):
        info_link = "https://api.gemini.com/v1/pubticker/ethusd"

        try:
            response = urllib.request.urlopen(info_link)
            data = json.loads(response.read().decode())
            price = data['last']
        except Exception:
            print("Failed Gemini")
            price = -1

        return str(price)

    def get_bid(self):
        info_link = "https://api.gemini.com/v1/pubticker/ethusd"

        try:
            response = urllib.request.urlopen(info_link)
            data = json.loads(response.read().decode())
            price = data['bid']
        except Exception:
            print("Failed Gemini")
            price = -1

        return str(price)

    def get_ask(self):
        info_link = "https://api.gemini.com/v1/pubticker/ethusd"

        try:
            response = urllib.request.urlopen(info_link)
            data = json.loads(response.read().decode())
            price = data['ask']
        except Exception:
            print("Failed Gemini")
            price = -1

        return str(price)

    def buy(self):
        return True

    def sell(self):
        return True

    def transfer(self):
        return True
