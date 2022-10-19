t = int(input())

for _ in range(t):
    N, C = list(map(int, input().split()))
    result = 0

    list1 = []
    for _ in range(N):
        W, V = list(map(int, input().split()))
        list1.append([W / V , W , V])
    
    list1.sort(reverse=True)

    for i in range(N):
        if C != 0:
            if list1[i][2] < C:
                result += list1[i][1]
                C -= list1[i][2]
            else:
                result += int(list1[i][0] * C)
                C -= C
        else:
            break
    
    print(result)