def func(N, M):
    l = [[] for _ in range(N)]
    for _ in range(M):
        i, j = list(map(int, input().split()))
        l[i].append(j)
        l[j].append(i)
    return l

t = int(input())
for _ in range(t):
    N, M = list(map(int, input().split()))
    result = func(N, M)
    for r in result:
        r.sort()
        print(*r)