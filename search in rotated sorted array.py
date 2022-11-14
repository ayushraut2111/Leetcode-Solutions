# https://leetcode.com/problems/search-in-rotated-sorted-array
class Solution:
    def search(self, nums,target):
        if target in nums:
            return nums.index(target)
        else:
            return -1