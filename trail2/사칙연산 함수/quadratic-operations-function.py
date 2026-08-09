a, o, c = input().split()

def adder(x, y):
    return x + y

def subber(x, y):
    return x - y

def multi(x, y):
    return x * y

def devider(x, y):
    return x // y

a = int(a)
c = int(c)
if not o in "+-/*":
    print("False")
else:
    if o == "+":
        print(f"{a} {o} {c} = {adder(a, c)}")
    elif o == "-":
        print(f"{a} {o} {c} = {subber(a, c)}")
    elif o == "*":
        print(f"{a} {o} {c} = {multi(a, c)}")
    else:
        print(f"{a} {o} {c} = {devider(a, c)}")