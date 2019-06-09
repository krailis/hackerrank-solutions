#!/bin/python3

import operator

# Complete the jimOrders function below.
def jimOrders(orders):
    timed_orders = []
    customer = 1
    for order in orders:
        timed_orders.append((order[0] + order[1], customer))
        customer += 1
    timed_orders.sort(key=operator.itemgetter(1))
    timed_orders.sort()
    return [x[1] for x in timed_orders]
    

if __name__ == '__main__':
    n = int(input())
    orders = []
    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))
    result = jimOrders(orders)
    print(' '.join(map(str, result)))

