# https://leetcode.com/problems/maximum-average-subarray-i

class Solution:
    def findMaxAverage(self, a):
        ans=-9999999
        s=sum(a[:k])
        ans=max(s,ans)
        for i in range(0,len(a)-k):
            s-=a[i]
            s+=a[i+k]
            ans=max(s,ans)
        return ans/k