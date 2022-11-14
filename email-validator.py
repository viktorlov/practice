def check(arg):
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, arg):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    email = input()
    check(email)
