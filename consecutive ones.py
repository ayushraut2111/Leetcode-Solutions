# https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        if max(nums)==0:
            return 0
        if len(nums)==1:
            if nums[0]==1:
                return 1
            return 0
        count=1
        ans=0
        for i in range(len(nums)-1):
            if nums[i]==1 and nums[i]==nums[i+1]:
                count+=1
            else:
                ans=max(ans,count)
                count=1
        ans=max(ans,count)
        return ans

        