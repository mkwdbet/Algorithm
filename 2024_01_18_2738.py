import numpy as np
n,m = map(int, input().split())
array_a = np.zeros(shape=(n,m))
array_b = np.zeros(shape=(n,m))
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        array_a[i,j] = a[j]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        array_b[i,j] = a[j]
result = array_a +array_b
for i in range(n):
    for j in range(m):
        print(result[n,m],end=" ")
print(result.shape)