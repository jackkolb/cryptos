from exchanges import *
import time
from arbitrage import *
from exchanges import Binance, Poloniex, GDAX, Gemini, SIMEX, Liquid, Bitlish, Bitstamp, CEX, itBit
import json, urllib.request


if __name__ == '__main__':
    print("Welcome to Cryptos Arbitrage")
    print("  Populating exchange dictionary")

    active_exchanges = {
        # "Binance": Binance.Binance(),  # restricted from USA
        "Poloniex": Poloniex.Poloniex(),
        "GDAX": GDAX.GDAX(),
        "Gemini": Gemini.Gemini(),
        "SIMEX": SIMEX.SIMEX(),
        "Liquid": Liquid.Liquid(),
        "Bitlish": Bitlish.Bitlish(),
        "Bitstamp": Bitstamp.Bitstamp(),
        "CEX": CEX.CEX(),
        "itBit": itBit.itBit()
    }

    print("  Regular scanning")

    while True:
        analyze(active_exchanges)
        time.sleep(10)
