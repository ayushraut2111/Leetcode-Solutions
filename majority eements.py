# https://leetcode.com/problems/majority-element-ii/
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        n=len(nums)
        n=n//3
        a=[]
        for key,value in dict.items():
            if value>n:
                a.append(key)
        return a