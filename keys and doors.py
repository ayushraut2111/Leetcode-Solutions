# https://leetcode.com/problems/keys-and-rooms/
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n=len(rooms)
        visited=[False for i in range(n)]
        stack=[0]
        visited[0]=True
        while len(stack)>0:
            x=stack.pop()
            for i in rooms[x]:
                if visited[i]==False:
                    stack.append(i)
                    visited[i]=True
        for i in visited:
            if i==False:
                return False
        return True