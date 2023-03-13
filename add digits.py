# https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        num=str(num)
        count=num
        while len(num)>1:
            count=0
            for i in num:
                count+=int(i)
            num=str(count)
        return count
