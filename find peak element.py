# https://leetcode.com/problems/find-peak-element/
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 0
        elif len(nums)==2:
            return nums.index(max(nums))
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        return nums.index(max(nums))