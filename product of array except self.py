# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if len(nums)==0:
            return nums
        if min(nums)==0 and max(nums)==0:
            return nums
        pr=1
        x=1
        for i in range(len(nums)):
            x*=nums[i]
            if nums[i]!=0:
                pr*=nums[i]
        c=nums.count(0)
        ans=[]
        for i in range(len(nums)):
            if nums[i]==0 and c==1:
                ans.append(pr)
            elif nums[i]==0:
                ans.append(0)
            else:
                ans.append(x//nums[i])
        return ans

s=Solution()
print(s.productExceptSelf([1,2,3,4]))