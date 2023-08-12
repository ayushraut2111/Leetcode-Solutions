# https://leetcode.com/problems/find-all-duplicates-in-an-array
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        maxi=max(nums)
        visited=[0 for i in range(maxi+1)]
        ans=[]
        for i in nums:
            visited[i]+=1
            if visited[i]==2:
                ans.append(i)
        return ans