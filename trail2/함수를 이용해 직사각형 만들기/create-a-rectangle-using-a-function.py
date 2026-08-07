n, m = map(int, input().split())

def make_rect(row, col):
    for i in range(row):
        print("1" * col)

make_rect(n, m)