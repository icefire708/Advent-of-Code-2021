with open('7.txt', 'r') as f:
    positions = list(map(int, f.read().split(',')))
fuel = float('inf')
for x in range(0, 2000):
    current = 0
    for pos in positions:
        n = abs(pos - x)
        current += (1 + n) * n // 2
    if current < fuel:
        fuel = current
print(fuel)