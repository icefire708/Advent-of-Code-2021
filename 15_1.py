with open('15.txt', 'r') as f:
    data = [[float('inf')] + list(map(int, x)) for x in f.read().split()]
data.insert(0, [float('inf')] * len(data[0]))
data[1][1] = 0
for i in range(1, len(data)):
    for j in range(1, len(data[0])):
        if i == j == 1:
            continue
        data[i][j] += min(data[i - 1][j], data[i][j - 1])
print(data[-1][-1])
# тут не учтена возможность идти влево и вверх