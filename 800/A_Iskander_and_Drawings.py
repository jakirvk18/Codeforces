for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    count = 0
    ans = 0
    for ch in s:
        if ch == '#':
            count += 1
            ans = max(ans, count)
        else:
            count = 0
    print((ans + 1) // 2)
