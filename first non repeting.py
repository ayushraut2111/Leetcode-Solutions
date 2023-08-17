# https://leetcode.com/problems/first-unique-character-in-a-string
class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp={}
        for i in s:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        for i in range(len(s)):
            if mp[s[i]]==1:
                return i
        return -1