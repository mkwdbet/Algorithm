import itertools
N,S = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0
for i in range(1,N+1):
    combs = itertools.combinations(nums,i)
    for j in combs: 
        if sum(list(j)) == S:
            cnt+=1
print(cnt)


