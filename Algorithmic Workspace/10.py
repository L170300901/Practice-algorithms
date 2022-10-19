def cost(A, B):
  distance = 0
  for i in range(len(A)):
    for j in range(i+1,):
        distance += abs(A[i] - A[j]) + abs(B[i] - B[j])
        
  return distance

t = int(input())
for _ in range(t):
    n = int(input())
    result = 0
    l_x = []
    l_y = []
    for _ in range(n):
        x , y = list(map(int, input().split()))
        l_x.append(x)
        l_y.append(y)
    cost(l_x , l_y)
    print(l_x , l_y)



