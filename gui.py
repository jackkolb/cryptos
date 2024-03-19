from tkinter import *
from threading import Thread
from exchanges import Binance, Poloniex, GDAX, Gemini, SIMEX, Liquid, Bitlish, Bitstamp, CEX, itBit


window = Tk()

window.title("Arbitrage Portal")

title = Label(window, text="Arbitrage Portal")

title_exchange = Label(window, text="Exchange")
title_exchange.grid(column=0, row=1)

title_ask = Label(window, text="Ask")
title_ask.grid(column=1, row=1)

title_bid = Label(window, text="Bid")
title_bid.grid(column=2, row=1)


exchanges = [
    # Binance.Binance(),
    # Bitlish.Bitlish(),
    Bitstamp.Bitstamp(),
    CEX.CEX(),
    GDAX.GDAX(),
    Gemini.Gemini(),
    # itBit.itBit(),
    # Liquid.Liquid(),
    # Poloniex.Poloniex(),
    # SIMEX.SIMEX()
]

exchange_name_labels = []
exchange_bid_labels = []
exchange_ask_labels = []

for exchange in exchanges:
    name_label = Label(window, text=exchange.get_name())
    name_label.grid(column=0, row=len(exchange_name_labels)+2)

    ask_label = Label(window)
    ask_label.grid(column=1, row=len(exchange_ask_labels)+2)

    bid_label = Label(window)
    bid_label.grid(column=2, row=len(exchange_bid_labels)+2)

    exchange_name_labels.append(name_label)
    exchange_bid_labels.append(bid_label)
    exchange_ask_labels.append(ask_label)

def getPrice(exchange, i, ask):
    if ask:
        return round(float(exchange.get_ask()), 2)
    else:
        return round(float(exchange.get_bid()), 2)

def getPrices():
    threads = []
    for i in range(len(exchanges)):
        bid_thread = Thread(target=getPrice, args=[exchanges[i], i, False])
        ask_thread = Thread(target=getPrice, args=[exchanges[i], i, True])
        threads.append(bid_thread)
        threads.append(ask_thread)
        bid_thread.start()
        ask_thread.start()

    for thread in threads:
        thread.join()

    return


def update():
    bids = []
    asks = []

    for exchange in exchanges:
        bids.append(exchange.get_bid())
        asks.append(exchange.get_ask())

    for i in range(len(bids)):
        exchange_bid_labels[i]["text"] = bids[i]
        exchange_ask_labels[i]["text"] = asks[i]

        exchange_bid_labels[i]["bg"] = "white"
        exchange_ask_labels[i]["bg"] = "white"

    min_bid_index = bids.index(min(bids))
    max_ask_index = asks.index(max(asks))

    exchange_bid_labels[min_bid_index]["bg"] = "blue"
    exchange_ask_labels[max_ask_index]["bg"] = "green"

    title.after(1000, update)


title.grid(column=0, row=0)

update()

window.mainloop()