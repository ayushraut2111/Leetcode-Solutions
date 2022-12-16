class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        a=p.split('*')
        aas=s[0]
        if a[0]=='':
            for i in range(1,len(s)):
                j=i-1
                if s[i]!=s[j]:
                    break
                else:
                    aas+=s[j]
        aal=s[-1]
        if a[-1]=='':
            for i in range(len(s)-1,0,-1):
                j=i-1
                if s[i]!=s[j]:
                    break
                else:
                    aal+=s[j]

        # print(aas,aal)
        
        pass
        

if __name__=="__main__":
    s=input()
    p=input()
    s=Solution().isMatch(s,p)
    if s:
        print("YES")
    else:
        print("NO")