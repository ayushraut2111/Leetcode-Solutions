# https://leetcode.com/problems/single-number-iii/
class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        mp={}
        for i in nums:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        ans=[]
        for key,value in mp.items():
            if value==1:
                ans.append(key)
            if len(ans)==2:
                return ans