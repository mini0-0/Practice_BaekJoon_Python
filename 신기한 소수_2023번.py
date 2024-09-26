import sys
import math
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

N = int(input())

def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i ==0:
            return False
    return True


def DFS(number):
    if len(str(number)) == N:
        print(number)

    else:
        for i in range(1, 10):
            if i %2 == 0:
                continue
            if isPrime(number*10 + i):
                DFS(number*10+i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)