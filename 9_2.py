def find_it(mat, x, y):
    if mat[x][y] >= 9:
        return 0
    mat[x][y] = 11
    return 1 + find_it(mat, x, y + 1) + find_it(mat, x + 1, y) + find_it(mat, x, y - 1) + find_it(mat, x - 1, y)


mat = []
with open('9.txt', 'r') as f:
    for row in f.readlines():
        mat.append([10] + list(map(int, row.strip())) + [10])
mat.insert(0, [10] * len(mat[0]))
mat.append([10] * len(mat[0]))
basines = []
for i in range(1, len(mat) - 1):
    for j in range(1, len(mat[0]) - 1):
        if (mat[i][j] < mat[i + 1][j] and mat[i][j] < mat[i - 1][j] 
            and mat[i][j] < mat[i][j - 1] and mat[i][j] < mat[i][j + 1]):
                basines.append(find_it(mat, i, j))
basines.sort()
print(basines[-1] * basines[-2] * basines[-3])