# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        a=[0 for i in range(len(nums)+1)]
        for i in nums:
            a[i]+=1
        for i in a:
            if i==0:
                return a.index(i)