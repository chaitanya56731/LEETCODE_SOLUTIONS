class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l=0
        seen ={}
        for r,ch in enumerate(s):
            if ch in seen and  seen[ch] >= l:
                l = seen[ch]+1
            seen[ch] = r
            res = max(res,r-l+1)
        return res

        