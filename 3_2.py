with open('3.txt', 'r') as f:
    numbers = f.read().split()
for i in range(len(numbers[0])):
    count = 0
    zeros = []
    ones = []
    for number in numbers:
        digit = int(number[i])
        count += digit
        if digit:
            ones.append(number)
        else:
            zeros.append(number)
    if count >= len(numbers) - count:
        numbers = ones
    else:
        numbers = zeros
    if len(numbers) == 1:
        break
oxygen_generator_rating = int(numbers[0], base=2)

with open('3.txt', 'r') as f:
    numbers = f.read().split()
for i in range(len(numbers[0])):
    count = 0
    zeros = []
    ones = []
    for number in numbers:
        digit = int(number[i])
        count += digit
        if digit:
            ones.append(number)
        else:
            zeros.append(number)
    if count >= len(numbers) - count:
        numbers = zeros
    else:
        numbers = ones
    if len(numbers) == 1:
        break
CO2_scrubber_rating = int(numbers[0], base=2)

print(oxygen_generator_rating * CO2_scrubber_rating)
