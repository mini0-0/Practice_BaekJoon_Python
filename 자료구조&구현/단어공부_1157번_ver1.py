import sys
from collections import defaultdict
input = sys.stdin.readline

alpha = input().strip().upper()
dic = defaultdict(int)

for a in alpha:
       dic[a] += 1

max_value = max(dic.values())
max_keys = [k for k, v in dic.items() if v == max_value]

if len(max_keys) > 1:
    print("?")
else:
    print(max_keys[0])