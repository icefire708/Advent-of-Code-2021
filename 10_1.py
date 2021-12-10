score = 0
d = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
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
                score += d[x]
                break
print(score)