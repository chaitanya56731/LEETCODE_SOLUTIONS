class Solution:
    def jump(self,nums):
        jumps = 0
        currEnd = 0
        currFarthest = 0
        for i in range(len(nums)-1):
            currFarthest = max(currFarthest,i+nums[i])
            if i == currEnd:
                jumps += 1
                currEnd = currFarthest
        return jumps

