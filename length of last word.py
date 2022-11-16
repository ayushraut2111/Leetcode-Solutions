# https://leetcode.com/problems/length-of-last-word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        i=len(s)-1
        count=0
        while i>=0 and s[i]!=' ':
            count+=1
            i-=1
        return count