class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0]= True
        for i in range(len(s)):
            if dp[i]:
                for w in wordset:
                    if s.startswith(w,i):
                        dp[i+len(w)]=True
        return dp[-1]
        