# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def st(self,left,right,s,n,ans):
        if len(s)==n*2:
            ans.append(s)
            return
        if left<n:
            self.st(left+1,right,s+'(',n,ans)
        if right<left:
            self.st(left,right+1,s+')',n,ans)
        
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        self.st(0,0,'',n,ans)
        return ans