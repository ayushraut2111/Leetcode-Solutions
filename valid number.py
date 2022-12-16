# https://leetcode.com/problems/valid-number
class Solution:
    def isNumber(self, s):
        if s=='inf' or s=="-inf" or s=="+inf" or s=="Infinity" or s=="-Infinity" or s=="+Infinity":
            return False
        try:
            float(s)
        except ValueError:
            return False
        
        return True