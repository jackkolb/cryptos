import statistics


def analyze(exchanges):
    exchange_names = list([exchanges[exchange].get_name() for exchange in exchanges.keys()])
    asks = []
    for exchange in exchanges:
        print("    Scanning", exchange)
        asks.append(exchanges[exchange].get_ask())
    print("Asks:", ", ".join(asks))
    bids = list([exchanges[exchange].get_bid() for exchange in exchanges.keys()])

    analysis = dict()

    # generate permutations of profitable pairs
    profitable_pairs = []
    for buy_exchange in exchanges.keys():
        buy_exchange = exchanges[buy_exchange]
        if not buy_exchange.can_buy:
            continue

        for sell_exchange in exchanges.keys():
            sell_exchange = exchanges[sell_exchange]
            if not sell_exchange.can_sell:
                continue
            trade = dict()

            # set exchanges
            trade["buy"] = buy_exchange.get_name()
            trade["sell"] = sell_exchange.get_name()

            # collect buy/sell prices (using those just collected)
            buy_price = asks[exchange_names.index(buy_exchange.get_name())]
            sell_price = bids[exchange_names.index(sell_exchange.get_name())]

            # if there were any price collection failures, skip
            if buy_price == -1 or sell_price == -1 or isinstance(sell_price, str):
                #print("Price collection failure")
                continue

            # simulate an exchange, test profitability

            # buy eth
            initial_usd = 1
            eth = initial_usd / float(buy_price)

            # buy fees
            eth = eth * (1 - buy_exchange.buy_fee_percentage)

            # withdraw fees
            eth = eth * (1 - buy_exchange.withdraw_fee_percentage)

            # deposit fees
            eth = eth * (1 - sell_exchange.deposit_fee_percentage)

            # sell fees
            eth = eth * (1 - sell_exchange.sell_fee_percentage)

            # sell eth
            final_usd = eth * float(sell_price)

            # check if still profitable
            if final_usd - initial_usd <= 0.0:
                continue

            profit_ratio = final_usd / initial_usd

            trade["profit"] = profit_ratio

            profitable_pairs.append(trade)

    analysis["profitable pairs"] = profitable_pairs

    # find most profitable pairs
    most_profitable_buy = "none"
    most_profitable_sell = "none"
    most_profitable_profit = -1
    for trade in profitable_pairs:
        if trade["profit"] > most_profitable_profit:
            most_profitable_buy = str(trade["buy"])
            most_profitable_sell = str(trade["sell"])
            most_profitable_profit = trade["profit"]

    analysis["most profitable buy"] = most_profitable_buy
    analysis["most profitable sell"] = most_profitable_sell
    analysis["most profitable profit"] = most_profitable_profit

    if most_profitable_buy == "none":
        print("    No profitable trades currently")
    else:
        print("    Buy from " + most_profitable_buy + ", sell to " + most_profitable_sell + " for " + str(most_profitable_profit))


    return analysis

