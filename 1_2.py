with open('1.txt', 'r') as f:
    numbers = list(map(int, f.read().split()))
prev_sum = numbers[0] + numbers[1] + numbers[2]
res = 0
for i in range(3, len(numbers)):
    next_sum = prev_sum + numbers[i] - numbers[i - 3]
    res += int(prev_sum < next_sum)
print(res)