n = int(input())
stack = []
answer = []
flag = 0
count = 1
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        answer.append("+")
        count += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)

# n = int(input())
# A = [0] * n
#
# for i in range(n):
#     A[i] = int(input())
#
# stack = []
# num = 1
# result = True
# answer = []
# for i in range(n):
#     su = A[i]
#     if su >= num:
#         while su >= num:
#             stack.append(num)
#             num += 1
#             answer.append('+')
#         stack.pop()
#         answer.append('-')
#
#     else:
#         m = stack.pop()
#         if m > su:
#             print('NO')
#             result = False
#             break
#
#         else:
#             answer.append('-')
#
# if result:
#     for i in answer:
#         print(i)