class Solution:
    def __init__(self):
        self.ans=[]
    def minWindow(self, s: str, t: str):
        s=list(s)
        t=list(t)
        # print(s,t)
        if len(t)>len(s):
            return ""
        dict={}
        for i in t:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        n=[]
        # print(len(t),len(n))
        count=0
        for i in range(len(t),len(s)):
            count=0
            n=s[:i]
            # print(n)
            di={}
            for l in n:
                if l not in di:
                    di[l]=1
                else:
                    di[l]+=1
            for key,value in dict.items():
                if key not in di:
                    break
                elif value==di[key]:
                    count+=1
            if count==len(dict):
                self.ans.append("".join(n))
            for j in range(i,len(s)):
                count=0
                if s[j] in di:
                    di[s[j]]+=1
                else:
                    di[s[j]]=1
                di[s[i-len(n)]]-=1
                for key,value in dict.items():
                    if key not in di:
                        break
                    elif value==di[key]:
                        count+=1
                if count==len(dict):
                    self.ans.append("".join(n))
        self.ans.sort(key=len)
        print(self.ans)
        try:
            return self.ans[0]
        except:
            return ""


if __name__=="__main__":
    s=input()
    p=input()
    s=Solution().minWindow(s,p)
    print(s)