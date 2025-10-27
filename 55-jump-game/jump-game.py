class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for x,i in enumerate(nums):
            if x > reach : return False
            reach= max(reach,i+x)
        return True