# https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def ispath(self,graph,visited,i):
        visited[i]=True
        for x in graph[i]:
            if visited[x]==False:
                self.ispath(graph,visited,x)

    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph=[[] for i in range(n)]
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        visited=[False for i in range(n)]
        self.ispath(graph,visited,source)
        return visited[destination]
