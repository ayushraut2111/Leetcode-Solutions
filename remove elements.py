# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums[nums.index(val)]=-1
        # print(nums)
        dict={}
        for i in nums:
            if i!=-1:
                if i not in dict:
                    dict[i]=1
                else:
                    dict[i]+=1
        for i in range(len(nums)):
            nums[i]=-1
        i=0
        for key,value in dict.items():
            for j in range(i,i+value):
                nums[j]=key
            i+=value
        return len(nums)-nums.count(-1)

