# https://leetcode.com/problems/number-complement/
class Solution:
    def findComplement(self, num: int) -> int:
        x=bin(num)[2:]
        x=list(str(x))
        for i in range(len(x)):
            if x[i]=='1':
                x[i]='0'
            else:
                x[i]='1'
        x=''.join(x)
        print(x)
        return int(x,2)