import itertools

N = int(input())
nums = list(map(int,input().split()))
operators = list(map(int,input().split()))

op_list = []
for i in range(len(operators)):
    for j in range(operators[i]):
        op_list.append(i)

op_perms = itertools.permutations(op_list)

nums.reverse()
def calc(opers,nums):
    if len(opers) == 0:
        return nums[0]
    op = opers[0]
    num = nums[0]
    if op == 0:
        return calc(opers[1:],nums[1:]) +  num
    elif op == 1:
        return calc(opers[1:],nums[1:]) -  num
    elif op == 2:
        return calc(opers[1:],nums[1:]) *  num
    elif op == 3:
        return calc(opers[1:],nums[1:]) // num
max = -int(1e9)
min = int(1e9)

for op_perm in op_perms:
    result = calc(op_perm,nums)
    if result > max:
        max = result
    if result < min:
        min = result
print(max)
print(min)

