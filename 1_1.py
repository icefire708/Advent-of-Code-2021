with open('1.txt', 'r') as f:
    numbers = list(map(int, f.read().split()))
res = 0
for i in range(1, len(numbers)):
    res += int(numbers[i - 1] < numbers[i])
print(res)