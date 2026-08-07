arr = [list(map(int, input().split()))[:4] for _ in range(4)]
res = 0
for row in range(len(arr)):
    res += sum(arr[row][:row+1])
print(res)