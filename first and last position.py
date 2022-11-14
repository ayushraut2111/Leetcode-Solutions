#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if target not in nums:
            return [-1,-1]
        first,last=-1,-1
        count=0
        for i in range(len(nums)):
            if nums[i]==target and count==0:
                first=i
                last=i
                count+=1
            elif nums[i]==target and count==1:
                last=i
        return [first,last]
            