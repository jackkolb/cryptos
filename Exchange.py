class Exchange:

    def __init__(self,
                 api_key,
                 api_secret,
                 buy_fee,
                 sell_fee,
                 coinwatch,
                 get_price,
                 buy,
                 sell,
                 transfer):

        self.api_key = api_key
        self.api_secret = api_secret

        self.buy_fee = buy_fee
        self.sell_fee = sell_fee

        self.coinwatch = coinwatch

        self.get_price = get_price
        self.buy = buy
        self.sell = sell
        self.transfer = transfer


def initializeExchanges():
    exchanges = {}

    return exchanges
