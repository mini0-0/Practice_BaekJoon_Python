from queue import PriorityQueue
n = int(input())
A = PriorityQueue()

for _ in range(n):
    A.put(int(input()))

data1 = 0
data2 = 0
sum = 0

while A.qsize() > 1:
    data1 = A.get()
    data2 = A.get()
    temp = data1 + data2
    sum += temp
    A.put(temp)

print(sum)