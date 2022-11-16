# https://leetcode.com/problems/multiply-strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dt={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        count=1
        n1,n2=0,0
        for i in reversed(num1):
            n1+=dt[i]*count
            count*=10
        count=1
        for i in reversed(num2):
            n2+=dt[i]*count
            count*=10
        return str(n1*n2)