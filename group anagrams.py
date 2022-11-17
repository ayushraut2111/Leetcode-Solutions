# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs)==0:
            return [strs]
        ans=[]
        for i in range(len(strs)):
            if strs[i]!='#':
                p=[strs[i]]
                res1 = ''.join(sorted(strs[i]))
                for j in range(i,len(strs)):
                    res2 = ''.join(sorted(strs[j]))
                    if res1==res2:
                        p.append(strs[j])
                        strs[j]='#'
                p.pop(0)
                ans.append(p)
        return ans


s=Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))
