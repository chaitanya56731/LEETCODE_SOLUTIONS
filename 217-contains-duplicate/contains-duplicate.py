class Solution(object):
    def containsDuplicate(self, nums):
        see = set()
        for num in nums:
            if num in see:
                return True
            see.add(num)
        return False