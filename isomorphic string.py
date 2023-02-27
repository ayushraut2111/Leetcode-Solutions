# https://leetcode.com/problems/isomorphic-strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mp={}
        for i in range(len(s)):
            if s[i] in mp and t[i]!=mp[s[i]]:
                return False
            mp[s[i]]=t[i]
        f=set()
        for value in mp.values():
            f.add(value)
        if len(f)!=len(mp):
            return False
        temp=list(s)
        s=""
        for i in range(len(temp)):
            temp[i]=mp[temp[i]]
            s+=temp[i]
        if s==t:
            return True
        return False
        