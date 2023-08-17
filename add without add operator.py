# https://leetcode.com/problems/sum-of-two-integers/

import math
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x=int(math.log2(2**a*2**b))
        return x