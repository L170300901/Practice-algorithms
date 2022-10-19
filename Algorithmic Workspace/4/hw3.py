
# def funcB(num):
#     if num == 0:
#         return 1
#     return -(funcB(n-1)) + funcA(n-1) 
# def funcA(num):
#     if num == 0:
#         return 1
#     return (2 * funcA(n-1)) + funcB(n-1)


# t = int(input())

# for _ in range(t):
#     n = int(input())
#     list1 = [0 for _ in range(n+1)]
#     list2 = [0 for _ in range(n+1)]
#     print(funcA(n) % 20220824,funcB(n) % 20220824)

t = int(input())

for _ in range(t):
    n = int(input())
    A = [0 for _ in range(n+1)]
    B = [0 for _ in range(n+1)]
    A[0] = 1
    B[0] = 1
    for i in range(1,n+1):
        A[i] = (2 * A[i-1] + B[i-1]) %20220824
        B[i] = (- B[i-1] + A[i-1]) %20220824
    print(A[n],B[n])