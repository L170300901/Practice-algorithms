
def func(n):
    if n==1:
        result = 1
    elif n==2:
        result = 1
    else:
        result = func(n-1) + func(n-2)
    return result
t = int(int(input()))
for _ in range(t):
    a = int(int(input()))
    print(func(a))