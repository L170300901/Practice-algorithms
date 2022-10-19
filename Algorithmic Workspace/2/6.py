def func(left, right):
    # 첫번째 리스트
    cnt1 = 0
    len1 = len(left)
    # 두번째 리스트
    cnt2 = 0
    len2 = len(right)
    result = []
    while cnt1 < len1 or cnt2 < len2 :
        if cnt1 < len1 and cnt2 < len2 :
            # 두번째 리스트의 숫자가 더 클때.
            if left[cnt1] <= right[cnt2]:
                result.append(1)
                cnt1 += 1
            # 첫번째 리스트의 숫자가 더 클때.
            else:
                result.append(2)
                cnt2 += 1
        # 리스트 하나 다 돌렸는데 남을때: 비교를 할필요 없이 그냥 append
        elif cnt1 < len1:
            result.append(1)
            cnt1 += 1
        elif cnt2 < len2 :
            result.append(2)
            cnt2 += 1
    return result

t = int(input())
for _ in range(t):
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    print(*func(x, y))