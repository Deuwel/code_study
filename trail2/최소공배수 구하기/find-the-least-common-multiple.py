def lcm(n, m):
    temp_n, temp_m = n, m
    while temp_n % temp_m != 0:
        res = temp_n % temp_m
        temp_n, temp_m = temp_m, res
    gcd = temp_m
    return (n * m) // gcd

a, b = map(int, input().split())
print(lcm(a, b))