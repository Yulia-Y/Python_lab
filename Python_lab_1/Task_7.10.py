price = int(input())
flag_buy=flag_sell=False
while(price):
    last_price = price
    price = int(input())
    if last_price < price and not flag_buy:
        buy_price = price
        flag_buy = True
    if last_price > price and not flag_sell and flag_buy:
        sell_price = price
        flag_sell = True
print(buy_price, sell_price, sell_price - buy_price)
