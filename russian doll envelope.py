# https://leetcode.com/problems/russian-doll-envelopes/
class Solution:
    def maxEnvelopes(self, ev: list[list[int]]) -> int:
        ev.sort()
        count=1
        print(ev)
        i=0
        while i<len(ev)-1:
            for j in range(i+1,len(ev)):
                if ev[j][0]>ev[i][0] and ev[j][1]>ev[i][1] and ev[i]!=[]:
                    print(i,j)
                    ev[i]=[]
                    count+=1
                    i=j
                    if j==len(ev)-1:
                        return count
                    break
                elif j==len(ev)-1:
                    return count
            if i!=j:
                i+=1
        print(ev)
        return count
