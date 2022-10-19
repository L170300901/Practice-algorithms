n = int(input())
for _ in range(n):
    x = int(input())
    array1 = [0 for _ in range(x+1)]

    if n >= 4:
        array1[0] = 0
        array1[1] = 1
        array1[2] = 2
        array1[3] = 4

        for i in range(4, n+1):
            array1[i] = (array1[i-1] + array1[i-2] + array1[i-3]) % 1904101441

        print(array1[n])
    elif n == 3:
        print(4)
    elif n == 2:
        print(2)
    elif n == 1:
        print(1)
    else:
        print(0)