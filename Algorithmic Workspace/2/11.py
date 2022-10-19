def func(x):
    a= 0
    result = []
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            b = abs(x[i][1]-x[j][1])/abs(x[i][0]-x[j][0])
            if( b > a):
                a = b
                result = []
                result.append(x[i][0])
                result.append(x[i][1])
                result.append(x[j][0])
                result.append(x[j][1])
    print(*result)
t = int(input())  
for _ in range(t):         
    n = int(input())
    x = [list(map(int,input().split())) for i in range(n)]
    x.sort()
    func(x)
