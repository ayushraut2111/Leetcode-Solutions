# https://leetcode.com/problems/minimum-size-subarray-sum
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        s=sum(nums)
        if s<target:
            return 0
        i=0
        j=len(nums)-1
        l=len(nums)
        while i<j and s>target:
            print(i,j)
            if nums[i]<=nums[j]:
                s-=nums[i]
                i+=1
                print(nums[i])
            else:
                s-=nums[j]
                j-=1
                print(nums[j])
            # print(s)
            l-=1
        # print(s)  
        x=0
        if s<target:
            x=l+1
        else:
            x= l
        s=sum(nums)
        i=0
        j=len(nums)-1
        l=len(nums)
        while i<j and s>target:
            print(i,j)
            if nums[i]<nums[j]:
                s-=nums[i]
                i+=1
                print(nums[i])
            else:
                s-=nums[j]
                j-=1
                print(nums[j])
            # print(s)
            l-=1
        # print(s)  
        x1=0 
        if s<target:
            x1=l+1
        else:
            x1= l
        return(min(x,x1))
        


s=Solution()
print(s.minSubArrayLen(7,[2,3,1,2,4,3]))