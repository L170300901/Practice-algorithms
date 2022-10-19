def func(n, A, B, C):
    if n == 0:
        return
    else:
        func(n-1, A, C, B)
        print(A, "->", C)
        func(n-1, B, A, C)
t = int(input())
for _ in range(t):
    n = int(input())
    func(n, 'A', 'B', 'C') 