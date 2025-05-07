import sys
from collections import defaultdict
input = sys.stdin.readline


N, M = map(int, input().split())
word_list = defaultdict(int)

for n in range(N):
    word = input().strip()
    if len(word) >= M:
        word_list[word] += 1

answer = sorted(word_list.items(), key=lambda x:(-x[1],-len(x[0]),x[0]))

for key, item in answer:
     print(key)