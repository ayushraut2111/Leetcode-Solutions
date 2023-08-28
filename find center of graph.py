# https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        n=len(edges)+2
        graph=[[] for i in range(n)]
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        visited=[False for i in range(n)]

        for i in range(len(graph)):
            if len(graph[i])==n-2:
                return i
