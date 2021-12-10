scores = []
d = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

with open('10.txt', 'r') as f:
    for row in f.readlines():
        stack = []
        for x in row.strip():
            if x in '({[<':
                stack.append(x)
            elif stack and (stack[-1] == '{' and x == '}' or stack[-1] == '(' and x == ')' 
                    or stack[-1] == '[' and x == ']' or stack[-1] == '<' and x == '>'):
                stack.pop()
            else:
                break
        else:
            score = 0
            for x in reversed(stack):
                score *= 5
                score += d[x]
            scores.append(score)
scores.sort()
print(scores[len(scores) // 2])
