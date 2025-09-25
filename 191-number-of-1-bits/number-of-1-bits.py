class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        t = sum(int(digit) for digit in binary)
        return t
        