from typing import Counter


with open('6.txt', 'r') as f:
    laternfishes = Counter(map(int, f.read().split(',')))
    for _ in range(256):
        new_laternfishes = Counter()
        for i in range(8):
            new_laternfishes[i] = laternfishes[i + 1]
        new_laternfishes[6] += laternfishes[0]
        new_laternfishes[8] = laternfishes[0]
        laternfishes = new_laternfishes
print(sum(laternfishes.values()))