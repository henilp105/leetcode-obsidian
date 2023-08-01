class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5: return 0
        c=0
        while n>=5:
            t = n//5
            c+=t
            n//=5
        return c