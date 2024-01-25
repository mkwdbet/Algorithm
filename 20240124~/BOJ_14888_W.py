import itertools
nums = []
class Calc():
    def __init__(self, p, m, t, d, nums):
        self.p = p
        self.m = m
        self.t = t 
        self.d = d
        self.nums = nums
        self.output = 0
        self.index = 0
    # def random(self,a,b):
    #     for i in range(4):

    def permutations(self):
        arrs = []
        self.count = [self.p, self.m, self.t, self.d]
        for i in self.count:
            for j in range(i):
                arrs.append(self.count.index(i))
        nPr = itertools.permutations(arrs, len(nums)-1)
        return nPr
    
    def calculate(self):
        perm = self.permutations()
        returns = []
        for i in perm:
            for j in i:
                if j == 0:
                    self.plus()
                elif j == 1:
                    self.minus()
                elif j == 2:
                    self.times()
                else:
                    self.division()
            returns.append(self.output)
            self.output = 0
        returns = [returns.max(),returns.min()]
        return returns

    def plus(self):
        self.output = nums[self.index] + nums[self.index +1]
        self.index +=2
    
    def minus(self):
        self.output = nums[self.index] - nums[self.index +1]
        self.index +=2
        
    def times(self):
        self.output = nums[self.index] * nums[self.index +1]
        self.index +=2

    def division(self):
        self.output = nums[self.index] / nums[self.index +1]
        self.index +=2
        
a = Calc(0 ,0 ,1 ,0,[5,6])
print(a.calculate())
        
        
        
        
        
