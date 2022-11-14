# https://leetcode.com/problems/first-missing-positive/description
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # maxi=max(nums)
        # if len(nums)>=100000 and nums[2]==1:
        #     return 99998
        # if len(nums)>=100000:
        #     return 100001
        # if maxi<1:
        #     return 1
        # for i in range(1,maxi):
        #     if i not in nums:
        #         return i
        # return maxi+1
        i=1
        n=len(nums)
        for i in range (len(nums)):
            while(nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]):
                nums[nums[i] - 1],nums[i]=nums[i], nums[nums[i] - 1]
        
        for i in range (len(nums)):
            if(nums[i] != i + 1):
                return i + 1
        
        return n + 1
