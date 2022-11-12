# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if x>=-2**31+1 and x<2**31-1:
            count=0
            if x<0:
                x=abs(x)
                count+=1
            if x==0:
                return x
            a=list(str(x).strip('0'))
            a.reverse()
            a= int("".join(a))
            x=a
            if x>=-2**31+1 and x<2**31-1:
                if count==0:
                    return a
                else:
                    return -a
            else:
                return 0
        else:
            return 0

sol=Solution()
print(sol.reverse(-123000))