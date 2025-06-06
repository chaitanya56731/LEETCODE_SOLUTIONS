class Solution(object):
    def totalNQueens(self, n):
        def dfs(qu,xy_diff,xy_sum):
            p=len(qu)
            if p == n:
                self.result += 1
                return None
            for q in range(n):
                if q not in qu and p-q not in xy_diff and p+q not in xy_sum:
                    dfs(qu+[q],xy_diff+[p-q],xy_sum+[p+q])
        self.result=0
        dfs([],[],[])
        return self.result
        
        