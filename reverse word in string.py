# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        a=s.split(" ")
        a=a[::-1]
        while '' in a:
            a.remove('')
        print(a)
        ans=""
        for i in a:
            ans+=i
            ans+=" "
        ans=ans.strip()
        return ans
