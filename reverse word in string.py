# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        a=[]
        p=""
        for i in s:
            if i!=' ':
                p+=i
            elif len(p)!=0 and i==' ':
                a.append(p)
                p=''
        if p!='':
            a.append(p)
        ans=""
        for i in a[::-1]:
            ans+=i
            ans+=" "
        return ans[:-1]
