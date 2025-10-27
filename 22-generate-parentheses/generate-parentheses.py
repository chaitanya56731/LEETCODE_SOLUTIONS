class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open,close,curr):
            if len(curr) == 2*n:
                res.append(curr)
                return
            if open < n:
                backtrack(open+1,close,curr+'(')
            if close < open:
                backtrack(open,close+1,curr+')')
        backtrack(0,0,"")
        return res

        