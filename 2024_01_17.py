#2798 블랙잭
import itertools
n,m = map(int, input().split())
nums = list(map(int,input().split()))
nCr = itertools.combinations(nums, 3)
nCr = list(nCr)
cards = []
for i in nCr:
    if sum(i) <= m:
        cards.append(sum(i))
print(max(cards))