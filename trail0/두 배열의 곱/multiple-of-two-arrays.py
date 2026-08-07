arr_A = [list(map(int, input().split())) for _ in range(3)]
no = input()
arr_B = [list(map(int, input().split())) for _ in range(3)]
mult = [[elemA * elemB for elemA, elemB in zip(rowA, rowB)] for rowA, rowB in zip(arr_A, arr_B)]
for row in mult:
    print(*row)