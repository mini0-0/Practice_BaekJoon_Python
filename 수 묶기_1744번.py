from queue import PriorityQueue
n = int(input())
plus_h = PriorityQueue()
minus_h = PriorityQueue()
one = 0
zero = 0
total = 0

for _ in range(n):
    data = int(input())
    if data > 1:
        plus_h.put(data * -1)
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        minus_h.put(data)

while plus_h.qsize() > 1:
    first = plus_h.get() * -1
    second = plus_h.get() * -1
    total += first * second

if plus_h.qsize() > 0:
    total += plus_h.get() * -1

while minus_h.qsize() > 1:
    first = minus_h.get()
    second = minus_h.get()
    total += first * second

if minus_h.qsize() > 0:
    if zero == 0:
        total += minus_h.get()

total += one
print(total)
