# https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        an=int(a,2)
        bn=int(b,2)
        sn=an+bn
        s=bin(sn)[2::]
        return str(s)