arr = [list(map(int, input().split()))[:4] for i in range(4)]
cnt = 0
for row in arr:
    for col in row:
        if col % 5 == 0:
            cnt += 1
print(cnt)