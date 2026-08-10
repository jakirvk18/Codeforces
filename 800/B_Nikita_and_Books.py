for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    carry = 0
    for i in range(n):
        a[i] += carry
        carry = 0
        value = i + 1
        if a[i] < value:
            print("NO")
            break
        carry = a[i] - value
        a[i] = value 
    else:
        print("YES")
