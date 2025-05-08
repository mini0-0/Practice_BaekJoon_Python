import sys
input = sys.stdin.readline

S = input().rstrip()
stack = []
answer = ''
tag = False

for s in S:
    if s == '<':
        while stack:
            answer += stack.pop()
        tag = True
        answer += s
    elif s == '>':
        tag = False
        answer += s

    elif tag:
        answer += s

    else:
        if s.isalnum():
            stack.append(s)

        elif s == ' ':
            while stack:
                answer += stack.pop()
            answer += ' '

while stack:
    answer += stack.pop()

print(answer)