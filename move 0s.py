# https://leetcode.com/problems/move-zeroes
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        a=nums.count(0)
        if len(nums)==a:
            return
        num=[i for i in nums if i!=0]
        i=0
        for i in range(len(num)):
            nums[i]=num[i]
        i+=1
        while i<len(nums):
            nums[i]=0
            i+=1
        