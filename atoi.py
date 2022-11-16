# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        a=""
        s=s.strip()
        count=0
        if len(s)==0:
            return 0
        if s[0]=='-' or s[0]=='+':
            i=1
            count+=1
        while i!=len(s) and s[i]>='0' and s[i]<='9':
            a+=s[i]
            i+=1
        if len(a)==0:
            return 0
        else:
            n=int(a)
            if count==1 and s[0]=='-':
                n=-1*n
            if n>=-2**31 and n<2**31:
                return n
            else:
                if count==1 and s[0]=='-':
                    return -2147483648
                else:
                    return 2147483647
                
