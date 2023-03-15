# https://leetcode.com/problems/bulls-and-cows
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        g=1
        x=0
        mp1={}
        for i in secret:
            if i not in mp1:
                mp1[i]=[g-1]
            else:
                mp1[i].append(g-1)
            g+=1
        mp2={}
        g=0
        for i in guess:
            if i not in mp2:
                mp2[i]=[g]
            else:
                mp2[i].append(g)
            g+=1
        y=0
        for key,values in mp2.items():
            if key in mp1:
                z=0
                for i in mp1[key]:
                    if i in values:
                        z+=1
                x+=z
                y+=(min(len(mp1[key]),len(values))-z)
        return str(x)+'A'+str(y)+'B'

        
