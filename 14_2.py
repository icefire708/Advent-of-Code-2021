from typing import Counter


rules = []
with open('14.txt', 'r') as f:
    template = f.readline().strip()
    f.readline()
    for line in f.readlines():
        a, b = line.strip().split(' -> ')
        rules.append((a, b))
pairs = Counter()
for i in range(len(template) - 1):
    pairs[template[i] + template[i + 1]] += 1
for _ in range(40):
    new_pairs = Counter()
    for a, b in rules:
        new_pairs[a[0] + b] += pairs[a]
        new_pairs[b + a[1]] += pairs[a]
    pairs = new_pairs
c = Counter()
for k, v in pairs.items():
    c[k[0]] += v
    c[k[1]] += v
print((max(c.values()) - min(c.values()))//2)
