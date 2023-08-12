# https://leetcode.com/problems/find-all-duplicates-in-an-array
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        visited=[0 for i in range(100000)]
        ans=[]
        for i in nums:
            visited[i]+=1
            if visited[i]==2:
                ans.append(i)
        return ans