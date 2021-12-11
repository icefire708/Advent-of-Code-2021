with open('11.txt', 'r') as f:
    octopuses = [[0] + list(map(int, x)) + [0] for x in f.read().split()]
octopuses.insert(0, [0] * len(octopuses[0]))
octopuses.append([0] * len(octopuses[0]))
def flash(lights, first=False) -> bool:
    mark = False
    for i in range(1, len(octopuses) - 1):
        for j in range(1, len(octopuses[0]) - 1):
            if lights[i][j] == '-' and first:
                octopuses[i][j] += 1
            elif lights[i][j] == '*':
                lights[i][j] = '@'
            if octopuses[i][j] > 9:
                lights[i][j] = '*'
                octopuses[i][j] = 0
                mark = True
    return mark
step = 0
count = 0
while count != 100:
    step += 1
    lights = [['-'] * len(octopuses[0]) for _ in octopuses]
    flash(lights, first=True)
    mark = True
    while mark:
        for i in range(1, len(octopuses) - 1):
            for j in range(1, len(octopuses[0]) - 1):
                if lights[i][j] == '*':
                    for row in range(i - 1, i + 2):
                        for col in range(j - 1, j + 2):
                            if octopuses[row][col] != 0:
                                octopuses[row][col] += 1
        mark = flash(lights)
    count = 0
    for row in lights:
        count += row.count('@')
    
print(step)
