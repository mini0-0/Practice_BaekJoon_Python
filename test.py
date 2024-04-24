import sys

def check_username(username):
    if len(username) > 20:
        return "|"
    for char in username:
        if not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
            return "|"

    return "P"

username = sys.stdin.readline().strip()

result = check_username(username)
print(result)
