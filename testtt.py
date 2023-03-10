

s="a"*40000

mp={}
ans=[]
for i in range(len(s)):
    if s[i]=='c':
        ans.append(['c',i])
    if s[i]=='d':
        ans.append(['d',i])
    if s[i] not in mp:
        mp[s[i]]=1
    else:
        mp[s[i]]+=1
ct=s.count("a")
ap="a"*20000
ap+='dc'
ap+='a'*20000
ap+='cd'
ap+='a'*20000
print(mp,len(s),ct)
print(ans)
mp2={}
ans2=[]
for i in range(len(ap)):
    if ap[i]=='c':
        ans2.append(['c',i])
    if ap[i]=='d':
        ans2.append(['d',i])
    if ap[i] not in mp2:
        mp2[ap[i]]=1
    else:
        mp2[ap[i]]+=1
print(mp2,ans2)