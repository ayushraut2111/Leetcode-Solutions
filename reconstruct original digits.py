# https://leetcode.com/problems/reconstruct-original-digits-from-english/
class Solution:
    def originalDigits(self, s: str) -> str:
        mp={}
        for i in s:
            if i not in mp:
               mp[i]=1
            else:
                mp[i]+=1
        ans=[]
        l=["zero","one","two","three","four","five","six","seven","eight","nine"]
        k={"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
        h=len(s)//3
        print(mp)
        while h>0:
            for words in l:
                p=len(words)
                count=0
                for i in words:
                    if i in mp and mp[i]>0:
                        # print(i)
                        # mp[i]-=1
                        count+=1
                    else:
                        break
                if count==p:
                    for j in words:
                        mp[j]-=1
                    ans.append(k[words])
            h-=1
        ans="".join(ans)
        return ans
