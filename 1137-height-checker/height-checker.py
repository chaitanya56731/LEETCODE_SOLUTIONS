class Solution:
    def heightChecker(self, heights):
        expected = sorted(heights)
        return sum(1 for i in range(len(heights)) if heights[i] != expected[i])

        
        