class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(',']':'[','}':'{'}
        result=[]
        for ch in s:
            if ch in "([{":
                result.append(ch)
            else:
                if not result or result[-1] != pairs[ch]:
                    return False
                result.pop()
        return not result

            