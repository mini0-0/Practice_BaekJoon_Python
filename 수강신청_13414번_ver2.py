import sys
from collections import OrderedDict
input = sys.stdin.readline

K, L = map(int, input().split())
order = OrderedDict()

for _ in range(L):
    id = input().strip()
    if id in order:
        del order[id]
    order[id] = True

for i, key in enumerate(order.keys()):
    if i == K:
        break
    print(key)