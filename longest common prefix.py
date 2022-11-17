# https://leetcode.com/problems/longest-common-prefix
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        strs.sort(key=len)
        s=strs[0]
        strs.pop(0)
        ans=[]

        d=""
        for i in range(len(s)):
            d+=s[i]
            count=0
            for k in strs:
                if d not in k or k.index(d)!=0:
                    count+=1
                    break
            if count==0:
                ans.append(d)
        ans.sort(key=len)
        # print(ans)
        if len(ans)==0:
            return ""
        return ans[len(ans)-1]

s=Solution()
strs=["flower","flow","flight"]
print(s.longestCommonPrefix(strs))
