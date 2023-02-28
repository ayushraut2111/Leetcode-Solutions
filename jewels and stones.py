# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        mp1={}
        for i in stones:
            if i not in mp1:
               mp1[i]=1
            else:
                mp1[i]+=1
        count=0
        for i in jewels:
            if i in mp1:
                count+=mp1[i]
        return count

