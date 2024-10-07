answer = 0
A = list(map(str, input().split("-")))

def mySum(i):
    total = 0
    temp = str(i).split("+")
    for i in temp:
        total += int(i)
    return total

for i in range(len(A)):
    temp = mySum(A[i])
    if i==0:
        answer += temp
    else:
        answer -= temp

print(answer)