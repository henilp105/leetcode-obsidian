import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:return False
        if (math.log(n) / math.log(4))%1==0:
            return True
        return False

        