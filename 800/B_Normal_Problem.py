for _ in range(int(input())):
    a = input().strip()
    a = a[::-1]
    b = ""
    for i in a:
        if i == 'p':
            b += 'q'
        elif i == 'q':
            b += 'p'
        else:
            b += i
    print(b)