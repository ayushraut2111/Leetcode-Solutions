# https://leetcode.com/problems/longest-palindromic-substring/
# only 71 testcase passing
class Solution:


    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        count=[]
        for i in range(len(s)):
            ans=""
            sn=""
            l=i
            r=len(s)-i-1
            while l<r:
                if s[l]==s[r]:
                    ans+=s[l]
                    sn+=s[r]
                    l+=1
                    r-=1
                else:
                    l+=1
                    if l==r:
                        ans+=s[l]
                    s1=ans+sn[::-1]
                    count.append(s1)
                    ans=""
                    sn=""
            if l==r:
                ans+=s[l]
            s1=ans+sn[::-1]
            count.append(s1)
        for i in range(len(s)):
            ans=""
            sn=""
            l=i
            r=len(s)-i-1
            while l<r:
                if s[l]==s[r]:
                    ans+=s[l]
                    sn+=s[r]
                    l+=1
                    r-=1
                else:
                    r-=1
                    if l==r:
                        ans+=s[l]
                    s1=ans+sn[::-1]
                    count.append(s1)
                    ans=""
                    sn=""

            if l==r:
                ans+=s[l]
            s1=ans+sn[::-1]
            count.append(s1)
        return max(count, key = len)
        