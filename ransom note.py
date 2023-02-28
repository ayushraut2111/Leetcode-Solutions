# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mp1={}
        mp2={}
        for i in ransomNote:
            if i not in mp1:
               mp1[i]=1
            else:
                mp1[i]+=1
        
        for i in magazine:
            if i not in mp2:
               mp2[i]=1
            else:
                mp2[i]+=1
        for key,value in mp1.items():
            if key not in mp2:
                return False
            if mp2[key]<value:
                return False
        return True