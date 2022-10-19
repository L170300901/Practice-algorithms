import collections

t = int(int(input()))

for _ in range(t):
    s = list(map(int, input().split()))
    queue = collections.deque([])
    for i in range(len(s)):
        if len(queue) == 0:
            queue.append(s[i])
        else:
            if s[i] != queue[0]:
                queue.append(s[i])
            elif s[i] == queue[0]:
                queue.popleft()

    if len(queue) == 0: 
        print('NO')
    else:               
        print('YES')
