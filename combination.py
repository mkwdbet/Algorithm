n,m  = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True) #내림차순 정렬

def combination(nums,n,r):
    combs = []
    nums_len = len(nums)
    for i in range(nums_len):
        for j in range(nums_len-1,i-1,-1):
            combs.append(nums[i-1:j])
        
    print(combs)
combination(nums,n,3)

# lis = [1,2,3]
# print(lis[0:2])?
# nums = [1,2,3,4]
# print(nums[0:2])