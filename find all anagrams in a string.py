# https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p)>len(s):
            return []
        dic={}
        ans=[]
        for i in p:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        temp={}
        for i in range(0,len(p)):
            if s[i] not in temp:
                temp[s[i]]=1
            else:
                temp[s[i]]+=1
        if temp==dic:
            # print(temp,dic)
            ans.append(0)
        k=len(p)
        for i in range(len(p),len(s)):
            if s[i] not in temp:
                temp[s[i]]=1
            else:
                temp[s[i]]+=1
            temp[s[i-k]]-=1
            if temp[s[i-k]]==0:
                del temp[s[i-k]]
            if temp==dic:
                print(temp,dic)
                ans.append(i-k+1)
        return ans