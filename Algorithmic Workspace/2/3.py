def func(l, num):
    start = 0
    end = len(l)-1
    while start <= end:
        mid = (start + end) // 2
        if l[mid] == num:
            break
        elif l[mid] > num:
            end = mid - 1
        elif l[mid] < num:
            start = mid + 1
    if start > end:
        return -1
    else:
        return mid
t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    daan = []
    for num in num_list:
        daan.append(func(l, num))
    
    print(*daan)