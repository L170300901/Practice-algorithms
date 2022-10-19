import bisect

def func(a, b):
    i = bisect.bisect_left(a, b)
    if i == 0:
        return a[0]
    elif i == len(a):
        return a[i-1]
    else:
        if a[i] == b:
            return a[i]
        elif b - a[i-1] <= a[i] - b:
            return a[i-1]
        elif b - a[i-1] > a[i] - b:
            return a[i]
t = int(input())
for _ in range(t):
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    result = [func(x, num) for num in y]
    print(*result) 