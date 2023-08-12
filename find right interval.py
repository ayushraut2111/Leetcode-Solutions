# https://leetcode.com/problems/find-right-interval/
class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        if len(intervals)==1 and intervals[0][0]==intervals[0][1]:
            return [0]
        p=intervals[::]
        p.sort()
        print(p)
        ans=[]
        for i in intervals:
            ind=p.index(i)
            if ind==len(p)-1:
                ans.append(-1)
                continue
            cnt=p[ind][1]
            j=0
            x=len(ans)
            for j in range(ind,len(p)):
                if p[j][0]>=cnt:
                    ans.append(intervals.index(p[j]))
                    break
            if j==len(p)-1 and len(ans)==x:
                ans.append(-1)
        return ans