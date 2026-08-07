a, b = map(int, input().split())

def contains_369(m):
    mList = list(str(m))
    return any(c in "369" for c in mList)

def is_multiple(n):
    return n % 3 == 0
    
cnt = 0
for i in range(a, b+1):
    if contains_369(i) or is_multiple(i):
        cnt += 1

print(cnt)