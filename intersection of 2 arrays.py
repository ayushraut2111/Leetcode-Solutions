# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s1=set(nums1)
        s2=set(nums2)
        dic={}
        for i in s1:
            if i in s2:
                dic[i]=min(nums1.count(i),nums2.count(i))
        ans=[]
        for key,values in dic.items():
            ans+=[key for i in range(values)]
        return ans