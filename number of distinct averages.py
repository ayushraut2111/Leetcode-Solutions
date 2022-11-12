# https://leetcode.com/problems/number-of-distinct-averages

class Solution:
    def distinctAverages(self, nums):
        nums.sort()
        n=nums
        n.reverse()
        a=[]
        for i in range(len(nums)//2):
            x=(nums[i]+nums[len(nums)-i-1])/2
            a.append(x)
        a=set(a)
        return len(a)
            