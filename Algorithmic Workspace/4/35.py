import sys

t = int(input())

for _ in range(t):
    n = int(input())

    a = [0 for _ in range(n+1)]

    if n >= 4:
        a[0] = 0
        a[1] = 1
        a[2] = 2
        a[3] = 4

        for i in range(4, n+1):
            a[i] = (a[i-1] + a[i-2] + a[i-3]) % 1904101441

        print(a[n])
    elif n == 3:
        print(4)
    elif n == 2:
        print(2)
    elif n == 1:
        print(1)
    else:
        print(0)