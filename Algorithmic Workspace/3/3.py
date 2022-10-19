from collections import deque
def func(List, M):
    for i in range(M):
        u , v = map(int,input().split())
        List[u].append(v)
    print(List)
    for i in range(N):
        List[i].sort()
    Check = [False]*N
    Queue = deque([0])
    while Queue:
        v = Queue.popleft()
        if Check[v] == True:
            continue
        Check[v] = True
        print(v,end=" ")
        for i in List[v]:
            if Check[i] == False:
                Queue.append(i)
    print("")
t=int(input())
for _ in range(t):
    N , M = map(int,input().split())
    List = [[] for _ in range(N)]
    func(List, M)
    