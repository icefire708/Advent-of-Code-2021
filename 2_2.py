x = y = 0
aim = 0
with open('2.txt', 'r') as f:
    for line in f.readlines():
        direction, delta = line.split()
        delta = int(delta)
        if direction == 'forward':
            x += delta
            y += aim * delta
        elif direction == 'up':
            aim -= delta
        else:
            aim += delta
print(x * y)