# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
            elif dict[i]<2:
                dict[i]+=1
            else:
                continue
        for i in range(len(nums)):
            nums[i]=-100000
        i=0
        for key,value in dict.items():
            for j in range(i,i+value):
                nums[j]=key
            i+=value
        return len(nums)-nums.count(-100000)