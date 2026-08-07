num = int(input())
arr = [[0] * num for _ in range(num)]

for i in range(num):
    if i % 2 == 0:
        for j in range(num):
            arr[j][i] = j + 1
    else:
        for j in range(num):
            arr[j][i] = num - j

for row in arr:
    for col in row:
        print(col, end="")
    print()
