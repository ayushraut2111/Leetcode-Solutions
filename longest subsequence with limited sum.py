# https://leetcode.com/problems/longest-subsequence-with-limited-sum
class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        ans=[]
        nums.sort()
        print(nums)
        for c in queries:
            leng=0
            count=0
            i=0
            while i<len(nums) and count<c:
                count+=nums[i]
                leng+=1
                i+=1
            if count>c:
                ans.append(leng-1)
            else:
                ans.append(leng)
        return ans
            
                
            