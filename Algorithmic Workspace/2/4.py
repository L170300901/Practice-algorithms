def func(n, k, m):
    if k <= 1:
        return (n**k) % m
    else:
        # 몫
        a = k//2
        # 짝수이면 
        if k % 2 == 0:
            return ( func(n, a, m)**2 ) % m
        else:
            return ( func(n, a, m)**2 * n ) % m
t = int(input())
for _ in range(t):
    n, k, m = list(map(int, input().split()))
    print(func(n, k, m))
