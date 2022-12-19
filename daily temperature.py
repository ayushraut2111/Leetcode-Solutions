# https://leetcode.com/problems/daily-temperatures
class Solution:
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        if len(t)==1:
            return [0]
        ans=[0]
        stack=[len(t)-1]
        for i in range(len(t)-2,-1,-1):
            while len(stack)>0 and t[stack[-1]]<=t[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(0)
            else:
                ans.append(stack[-1]-i)
            stack.append(i)
        ans.reverse()
        return ans
            