# https://leetcode.com/problems/super-pow/
class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        num=int("".join(list(map(str,b))))
        return pow(a,num,1337)