class Solution(object):
    def solveNQueens(self, n):
        def dfs(qu,xy_diff,xy_sum):
            p=len(qu)
            if p == n:
                result.append(qu)
                return None
            for q in range(n):
                if q not in qu and p-q not in xy_diff and p+q not in xy_sum:
                    dfs(qu+[q],xy_diff+[p-q],xy_sum+[p+q])
        result =[]
        dfs([],[],[])
        return[["."*i+"Q"+"."*(n-i-1) for i in sol]for sol in result]
        
        