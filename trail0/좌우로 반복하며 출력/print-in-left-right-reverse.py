num = int(input())
for i in range(num):
    row = list(range(1, num+1))
    if i % 2 == 1:
        row.reverse()
    for c in row:
        print(c, end="")
    print()
