# https://leetcode.com/problems/top-k-frequent-elements
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dt={}
        for i in nums:
            if i not in dt:
                dt[i]=1
            else:
                dt[i]+=1
        a=[]
        cdict=dict(sorted(dt.items(),key=lambda x:x[1], reverse=True))
        for key,value in cdict.items():
            if k!=0:
                a.append(key)
                k-=1
            else:
                break
        return a