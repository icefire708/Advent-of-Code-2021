martrices = []
with open('4.txt', 'r') as f:
    numbers = map(int, f.readline().split(','))
    matrix = []
    f.readline()
    for line in f.readlines():
        if not line.strip():
            martrices.append(matrix)
            matrix = []
        else:
            row = list(map(int, line.split()))
            matrix.append(row)

marks = []
for _ in range(len(martrices)):
    marks.append([[False for _ in range(5)] for _ in range(5)])

def find_index():
    for number in numbers:
        for i, matrix in enumerate(martrices):
            for y, row in enumerate(matrix):
                if number in row:
                    ind = row.index(number)
                    marks[i][y][ind] = True # мда
                    if all(marks[i][y]):
                        return number, i
                    for line in marks[i]:
                        if not line[ind]:
                            break
                    else:
                        return number, i
last, ind = find_index()
s = 0
for i in range(5):
    for j in range(5):
        if not marks[ind][i][j]:
            s += martrices[ind][i][j]
print(s * last)
