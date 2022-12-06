# https://leetcode.com/problems/contains-duplicate
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n=len(nums)
        nums=set(nums)
        if n==len(nums):
            return False
        else:
            return True