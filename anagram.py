# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[0 for i in range(256)]
        for i in s:
            a[ord(i)]+=1
        for i in t:
            a[ord(i)]-=1
        for i in a:
            if i!=0:
                return False
        return True