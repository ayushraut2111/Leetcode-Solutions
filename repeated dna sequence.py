# https://leetcode.com/problems/repeated-dna-sequences
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        dna=[]
        ans=[]
        mp={}
        for i in range(len(s)-10+1):
            dna=s[i:i+10]
            if dna not in mp:
                mp[dna]=1
            else:
                mp[dna]+=1
        # print(mp)
        for key,value in mp.items():
            if value>1:
                ans.append(key)
        return ans