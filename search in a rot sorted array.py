# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        if target in nums:
            return True
        return False