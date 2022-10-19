INF = float('inf')
t = int(input())
for _ in range(t):
    N , M = map(int,input().split())
    Matrix = [[0]*N for _ in range(N)]
    for i in range(M):
        u , v , c = map(int,input().split())
        Matrix[u][v] = c 
    D = [0] + [INF] * (N-1)
    check = [False] * N
    for iteration in range(N):
        Min = INF
        for i in range(N):
            if D[i] < Min and not check[i]:
                Min = D[i]
                idx = i
        if Min == INF: break
        check[idx] = True
        for i in range(N):
            if Matrix[idx][i] != 0 and D[idx] + Matrix[idx][i] < D[i]:
                D[i] = D[idx] + Matrix[idx][i]
    if (D[N-1] == INF):
        print('-1')
    else:
        print(D[N-1])