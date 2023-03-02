class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        x=len(words)*len(words[0])
        mp1={}
        for i in words:
            if i not in mp1:
                mp1[i]=1
            else:
                mp1[i]+=1
        a=s[:x]
        ans=[]
        l=len(words)
        count=0
        mp2={}
        wl=len(words[0])
        for i in range(0,len(a),wl):
            if a[i:i+wl] not in mp2:
                mp2[a[i:i+wl]]=1
            else:
                mp2[a[i:i+wl]]+=1
        if mp1==mp2:
            ans.append(0)
        for j in range(1,len(s)-x+1):
            mp2={}
            a=s[j:j+x]
            for i in range(0,len(a),wl):
                if a[i:i+wl] not in mp2:
                    mp2[a[i:i+wl]]=1
                else:
                    mp2[a[i:i+wl]]+=1
            if mp1==mp2:
                ans.append(j)
        return ans