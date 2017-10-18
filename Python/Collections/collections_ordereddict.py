from collections import OrderedDict

N = int(input())
items_bought = OrderedDict()
for _ in range(N):
    item_and_price = input().strip().split()
    item, price = " ".join(item_and_price[:-1]), int(item_and_price[-1])
    if item in items_bought.keys():
        items_bought[item] += price
    else:
        items_bought[item] = price
for item, price in items_bought.items():
    print(item + " " + str(price))
