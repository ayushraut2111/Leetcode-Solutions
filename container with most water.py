# https://leetcode.com/problems/container-with-most-water/submissions
class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans=0
        i=0
        j=len(height)-1
        while i<j:
            ans=max(ans,min(height[i],height[j])*(j-i))
            if height[i]<height[j]:
                i+=1
            elif height[i]>height[j]:
                j-=1
            else:
                i+=1
                j-=1
        return ans
s=Solution()
print(s.maxArea([1,4,2,3]))