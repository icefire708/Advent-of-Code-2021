ans = 0
with open('8.txt', 'r') as f:
    for line in f.readlines():
        _, output = line.split(' | ')
        for value in output.split():
            if len(value) in (2, 3, 4, 7):
                ans += 1
print(ans)