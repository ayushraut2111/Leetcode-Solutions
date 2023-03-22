# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
class Solution:
    def minScore(self, n: int, roads) -> int:
        visited=[False for i in range(n)]
        s=[]
        visited[0]=True
        ans=999999999
        d=[[] for i in range(n)]
        for i in roads:
            d[i[0]-1].append([i[1]-1,i[2]])
            d[i[1]-1].append([i[0]-1,i[2]])
        s.append(0)
        while len(s)>0:
            a=s.pop()
            visited[a]=True
            for i in d[a]:
                if visited[i[0]]==False:
                    s.append(i[0])
                ans=min(ans,i[1])
        return ans




