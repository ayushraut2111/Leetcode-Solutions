# https://leetcode.com/problems/ugly-number-ii
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s={1,2,3,4,5}
        p={2,3,4,5}
        while len(s)<=n*4:
            k=set()
            for i in p:
                k.add(i*2)
                s.add(i*2)
                k.add(i*3)
                s.add(i*3)
                k.add(i*5)
                s.add(i*5)
            p=k
        ans=0
        count=1
        s=list(s)
        s.sort()
        for i in s:
            if count==n:
                return i
            count+=1
