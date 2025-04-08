import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
cards = sorted(map(int, input().split()))
m = int(input())
targets = map(int, input().split())

count = Counter(cards)
result = [str(count[t]) for t in targets]
print(' '.join(result))