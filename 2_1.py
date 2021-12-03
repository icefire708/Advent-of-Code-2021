x = y = 0
with open('2.txt', 'r') as f:
    for line in f.readlines():
        direction, delta = line.split()
        delta = int(delta)
        if direction == 'forward':
            x += delta
        elif direction == 'up':
            y += delta
        else:
            y -= delta
print(x * y)