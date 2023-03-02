# https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        d=0
        count=1
        for i in range(len(digits)-1,-1,-1):
            d+=digits[i]*count
            count*=10
        # print(d)
        d+=1
        l=[]
        while d>0:
            l.append(d%10)
            d=d//10
        return l[::-1]
        

