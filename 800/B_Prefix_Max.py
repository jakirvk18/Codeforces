for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    prefix = [0] * n
    prefix[0] = max(a)
    for i in range(1, n):
        prefix[i] = max(prefix[i - 1], a[i])
    print(sum(prefix))