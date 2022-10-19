t = int(input())
for _ in range(t):
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    cnt = 0 
    for i in x:
        for j in y:
            if(j==i):
                cnt += 1
    print(cnt)
        