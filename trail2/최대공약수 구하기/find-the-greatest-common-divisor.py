a, b = map(int, input().split())

def gcd(n, m):
    while n % m != 0:
        res = n % m
        n, m = m, res
    return m

print(gcd(a, b))