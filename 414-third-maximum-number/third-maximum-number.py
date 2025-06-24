class Solution(object):
    def thirdMax(self, nums):
        nums=list(set(nums))
        n=len(nums)
        nums.sort()
        if n >= 3:
            return nums[-3]
        else:
            return nums[-1]
        
        