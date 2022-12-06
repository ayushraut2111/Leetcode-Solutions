# https://leetcode.com/problems/majority-element
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        n=len(nums)
        n=n//2
        for key,value in dict.items():
            if value>n:
                return key