for _ in range(int(input())):
    s = list(input().split())
    ans = ""
    for word in s:
        ans += word[0]
    print(ans)