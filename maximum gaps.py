# https://leetcode.com/problems/maximum-gap
class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        ans=-1
        for i in range(len(nums)-1):
            j=i+1
            ans=max(ans,abs(nums[i]-nums[j]))
        return ans