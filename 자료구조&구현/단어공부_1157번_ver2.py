from collections import Counter

word = input().strip().upper()
counter = Counter(word)

max_count = max(counter.values())
max_chars = [char for char, cnt in counter.items() if cnt == max_count]

print('?') if len(max_chars) > 1 else print(max_chars[0])