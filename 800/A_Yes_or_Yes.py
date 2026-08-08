def logical_or(a, b):
    if a == b:
        return 'N'
    else:
        return 'Y'
for _ in range(int(input())):
    s = input().strip()
    stack = []
    for i in s:
        if stack and (stack[-1] != 'Y' or i != 'Y'):
            stack[-1] = logical_or(stack[-1], i)
        else:
            stack.append(i)
    print("YES" if len(stack) == 1 else "NO")