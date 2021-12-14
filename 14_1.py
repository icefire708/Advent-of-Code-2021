from typing import Counter


rules = {}
with open('14.txt', 'r') as f:
    template = f.readline().strip()
    f.readline()
    for line in f.readlines():
        a, b = line.strip().split(' -> ')
        rules[a] = b
for i in range(10):
    new_template = template[0]
    for i in range(len(template) - 1):
        key = template[i] + template[i + 1]
        new_template += rules[key] + template[i + 1]
    template = new_template
c = Counter(template)
print(max(c.values()) - min(c.values()))
