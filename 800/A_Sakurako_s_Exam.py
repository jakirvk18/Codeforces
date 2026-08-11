for _ in range(int(input())):
    a, b = map(int, input().split())
    arr = [1] * a
    arr.extend([2] * b)
    def BT(arr, s, index, n):
        if index == n:
            if s == 0:
                return True
            return False
        return (BT(arr, s + arr[index], index + 1, n) or BT(arr, s - arr[index], index + 1, n))
    if BT(arr, 0, 0, len(arr)):
        print("YES")
    else:
        print("NO")
