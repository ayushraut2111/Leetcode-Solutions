# https://leetcode.com/problems/permutations/
from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[list(p) for p in permutations(nums)]
        return ans
        