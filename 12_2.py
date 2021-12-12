g = {}
with open('12.txt', 'r') as f:
    for row in f.readlines():
        a, b = row.strip().split('-')
        if a in g:
            g[a].append(b)
        else:
            g[a] = [b]
        if b in g:
            g[b].append(a)
        else:
            g[b] = [a]


def ways(way, mark):
    if way[-1] == 'end':
        return 1
    count = 0
    for x in g[way[-1]]:
        if x == 'start':
            continue
        if x.islower() and x in way:
            if not mark:
                count += ways(way[:] + [x], True)
            continue
        count += ways(way[:] + [x], mark)
    return count


c = ways(['start'], False)
print(c)
