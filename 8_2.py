ans = 0
with open('8.txt', 'r') as f:
    for line in f.readlines():
        patterns, output = line.split(' | ')
        patterns = patterns.split()
        ddd = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
        for elem in patterns:
            ddd[len(elem)].append(elem)
        a = set(ddd[3][0]) - set(ddd[2][0])
        ced = (set(ddd[7][0]) - set(ddd[6][0])) | (set(ddd[7][0]) - set(ddd[6][1])) | (set(ddd[7][0]) - set(ddd[6][2]))
        e = ced - set(ddd[4][0])
        g = (set(ddd[7][0]) - set(ddd[4][0])) - e - a
        d = (set(ddd[4][0]) - set(ddd[2][0])) & ced
        c = ced - d - e
        f = set(ddd[2][0]) - c
        b = set(ddd[7][0]) - a - c - d - e - f - g
        a = a.pop()
        b = b.pop()
        c = c.pop()
        d = d.pop()
        e = e.pop()
        f = f.pop()
        g = g.pop() 
        decoder = {
            ''.join(sorted((a, b, c, e, f, g))): 0,
            ''.join(sorted((c, f))): 1,
            ''.join(sorted((a, c, e, d, g))): 2,
            ''.join(sorted((a, c, d, f, g))): 3,
            ''.join(sorted((b, c, d, f))): 4,
            ''.join(sorted((a, b, d, f, g))): 5,
            ''.join(sorted((a, b, d, e, f, g))): 6,
            ''.join(sorted((a, c, f))): 7,
            ''.join(sorted((a, b, c, d, e, f, g))): 8,
            ''.join(sorted((a, b, c, d, f, g))): 9,
        }
        number = 0
        for i, val in enumerate(output.split()):
            val = ''.join(sorted(val))
            number = number * 10 + decoder[val]
        ans += number
print(ans)
