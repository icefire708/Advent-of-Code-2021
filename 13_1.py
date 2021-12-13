dots = []
folds = []
size = 0
with open('13.txt', 'r') as f:
    sss = f.readlines()
    for i, line in enumerate(sss):
        line = line.strip()
        if line:
            x, y = map(int, line.split(','))
            dots.append((x, y))
            size = max(size, x, y)
        else:
            break
    for i in range(i + 1, len(sss)):
        line = sss[i]
        left, value = line.split('=')
        folds.append((left[-1], int(value)))

size += 1
mat = [['.' for _ in range(size)] for _ in range(size)]
for x, y in dots:
    mat[y][x] = '#'
heigh = width = size


def hor(y_line):
    for i in range(y_line):
        for x in range(width):
            if mat[y_line * 2 - i][x] == '#':
                mat[i][x] = '#'

def vert(x_line):
    for y in range(heigh):
        for x in range(x_line):
            if mat[y][x_line * 2 - x] == '#':
                mat[y][x] = '#'

for fold_type, value in folds:
    if fold_type == 'y':
        hor(value)
        heigh = value
    else:
        vert(value)
        width = value
    break

ans = 0
for i in range(heigh):
    for j in range(width):
        if mat[i][j] == '#':
            ans += 1
print(ans)