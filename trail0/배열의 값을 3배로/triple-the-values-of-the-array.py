arr = [list(map(int, input().split())) for row in range(3)]
new_arr = [[elem*3 for elem in row] for row in arr]
for row in new_arr:
    print(*row)
    