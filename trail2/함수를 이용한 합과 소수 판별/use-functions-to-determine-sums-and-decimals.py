a, b = map(int, input().split())

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_sum_even(n):
    str_n = str(n)
    res = sum([int(x) for x in str_n])
    if res % 2 == 0:
        return True
    return False

cnt = 0
for i in range(a, b+1):
    if is_prime(i) and is_sum_even(i):
        cnt += 1

print(cnt)