class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        full_week_sum = (7*weeks*(weeks+7))//2
        rem = days*(weeks+1) + days * (days-1)/2
        return int(full_week_sum + rem)

        