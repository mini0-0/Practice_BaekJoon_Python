import sys
input = sys.stdin.readline

n=int(input())
N=sorted(map(int,input().split()))
m=int(input())
M=map(int,input().split())

def binary(l,N,start,end):
     if start>end:
          return 0
     m = (start+end)//2
     count=0
     if l==N[m]:
          return N[start:end+1].count(l)
     elif l<N[m]:
          return binary(l,N,start,m-1)
     else:
          return binary(l,N,m+1,end)
dic={}
for i in N:
     start=0
     end=len(N)-1
     if i not in dic:
          dic[i] = binary(i,N,start,end)

print(' '.join(str(dic[x]) if x in dic else '0' for x in M))

