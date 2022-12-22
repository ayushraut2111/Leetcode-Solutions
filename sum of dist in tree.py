# https://leetcode.com/problems/sum-of-distances-in-tree/
class Solution:
    def dij(self,i,vis,graph,dis):
        vis[i]=True
        for j in graph[i]:
            if vis[j]==False or dis[i]+1<dis[j]:
                dis[j]=min(dis[j],dis[i]+1)
                self.dij(j,vis,graph,dis)
    def ins(self,u,v,graph):
        graph[u].append(v)
        graph[v].append(u)
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        ans=[]
        graph=[[] for i in range(n)]
        for i in edges:
            self.ins(i[0],i[1],graph)
        # print(graph)
        # print(dist)
        visited=[[False]*n]*n
        dist=[[9999999999]*n for i in range(n)]
        for i in range(n):
            # visited=[False]*n
            # visited[i]=True
            dist[i][i]=0
            self.dij(i,visited[i],graph,dist[i])
            ans.append(sum(dist[i]))
        return ans
            