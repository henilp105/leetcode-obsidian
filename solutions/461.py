class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(int(i) for  i in bin(x^y)[2:])