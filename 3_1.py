count = 1
with open('3.txt', 'r') as f:
    ones_count = list(map(int, f.readline().strip()))
    for line in f.readlines():
        count += 1
        for i, bit in enumerate(line.strip()):
            ones_count[i] += int(bit)
gamma_rate = ''
epsilon_rate = ''
for elem in ones_count:
    if elem > count - elem:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'
print(int(epsilon_rate, base=2) * int(gamma_rate, base=2))

        