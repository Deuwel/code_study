def is_complete_num(n):
    if n % 2 == 0:
        return False
    if str(n)[-1] == "5":
        return False
    if n % 3 == 0 and n % 9 != 0:
        return False
    return True

a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if is_complete_num(i):
        cnt += 1
print(cnt)