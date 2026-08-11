for _ in range(int(input())):
    a = list(map(int, input().split()))
    if a[-1] != max(a):
        max_index = -1
        mx = float("-inf")
        for i in range(7):
            if a[i] > mx:
                max_index = i
                mx = a[i]
        temp = a[-1]
        a[-1] = a[max_index]
        a[max_index] = temp
    print(-1 * sum(a[:-1])  + a[-1])