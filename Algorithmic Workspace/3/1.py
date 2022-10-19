def func(N, M):
    l = [[0]*N for _ in range(N)]
    for _ in range(M):
        i, j, k = list(map(int, input().split()))
        l[i][j] = k
    return l

t = int(input())
for _ in range(t):
    N, M = list(map(int, input().split()))
    result = func(N, M)
    for r in result:
        print(*r)