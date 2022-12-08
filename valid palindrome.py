# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s.strip()
        c=[]
        for i in s:
            if i>='a' and i<='z' or i.isdigit():
                c.append(i)
        p=c[::-1]
        # print(p)
        if p==c:
            return True
        return False