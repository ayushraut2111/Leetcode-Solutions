# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t=s.split()
        mp={}
        j=0
        if len(pattern)!=len(t):
            return False
        for i in pattern:
            mp[i]=t[j]
            j+=1
        # print(mp)
        f=set()
        for value in mp.values():
            f.add(value)
        if len(f)!=len(mp):
            return False
        pattern=list(pattern)
        for i in range(len(pattern)):
            pattern[i]=mp[pattern[i]]
        if pattern==t:
            return True
        return False