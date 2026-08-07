r, c = map(int, input().split())
grid_A = [list(map(int, input().split()))[:c] for _ in range(r)]
grid_B = [list(map(int, input().split()))[:c] for _ in range(r)]
compare_grid = [[int(elemA != elemB) for elemA, elemB in zip(rowA, rowB)] for rowA, rowB in zip(grid_A, grid_B)]
for row in compare_grid:
    print(*row)