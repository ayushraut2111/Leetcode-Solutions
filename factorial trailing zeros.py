# https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution:
    def fact(self,i):
        if i==0 or i==1:
            return 1
        return i*self.fact(i-1)
    def trailingZeroes(self, n: int) -> int:
        f=self.fact(n)
        f=str(f)
        count=0
        # print(type(f))
        for i in range(len(f)-1,-1,-1):
            # print(f[i])
            if f[i]=='0':
                count+=1
            else:
                break
        return count