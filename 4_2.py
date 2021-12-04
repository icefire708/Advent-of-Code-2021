martrices = []
with open('4.txt', 'r') as f:
    numbers = list(map(int, f.readline().split(',')))
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
        print(number)
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
while martrices:
    last, ind = find_index()
    matrix = martrices[ind]
    matrix_marks = marks[ind]
    del(martrices[ind])
    del(marks[ind])

s = 0
for i in range(5):
    for j in range(5):
        if not matrix_marks[i][j]:
            s += matrix[i][j]
print(s * last)
