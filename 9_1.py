mat = []
with open('9.txt', 'r') as f:
    for row in f.readlines():
        mat.append([10] + list(map(int, row.strip())) + [10])
mat.insert(0, [10] * len(mat[0]))
mat.append([10] * len(mat[0]))
risk_lvls_sum = 0
for i in range(1, len(mat) - 1):
    for j in range(1, len(mat[0]) - 1):
        if (mat[i][j] < mat[i + 1][j] and mat[i][j] < mat[i - 1][j] 
            and mat[i][j] < mat[i][j - 1] and mat[i][j] < mat[i][j + 1]):
                risk_lvls_sum += mat[i][j] + 1
print(risk_lvls_sum)