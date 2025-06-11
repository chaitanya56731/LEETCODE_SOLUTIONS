class Solution:
    def isHappy(self, n: int) -> bool:
        sett =set()
        while n != 1:
            sett.add(n)
            n= sum([int(x)**2 for x in str(n)])
            if n in sett:
                return False
        return True
        