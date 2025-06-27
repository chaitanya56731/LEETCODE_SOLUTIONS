
class Solution(object):
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        
        while l < r:
            
            while l < r and s[l].isalnum() == False: 
                l += 1
            while r > l and s[r].isalnum() == False: 
                r -= 1
            if l > r or s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

                    
           