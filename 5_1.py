horizontal_lines = []
vertical_lines = []
side = 0
with open('5.txt', 'r') as f:
    for line in f.readlines():
        a1, a2 = line.split(' -> ')
        x1, y1 = map(int, a1.split(','))
        x2, y2 = map(int, a2.split(','))
        if y1 == y2:
            x1, x2 = sorted([x1, x2])
            horizontal_lines.append(((x1, y1), (x2, y2)))
        elif x1 == x2:
            y1, y2 = sorted([y1, y2])
            vertical_lines.append(((x1, y1), (x2, y2)))
        side = max(side, x1, x2, y1, y2)
side += 1
field = [[0 for _ in range(side)] for _ in range(side)]
for (x1, y1), (x2, y2) in horizontal_lines:
    for x in range(x1, x2 + 1):
        field[y1][x] += 1
for (x1, y1), (x2, y2) in vertical_lines:
    for y in range(y1, y2 + 1):
        field[y][x1] += 1
print(sum(sum(int(field[x][y] > 1) for x in range(side)) for y in range(side)))

    