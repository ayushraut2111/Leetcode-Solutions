# https://leetcode.com/problems/string-compression/
class Solution:
    def compress(self, chars: list[str]) -> int:
        mp={}
        for i in chars:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        count=1
        ap=[]
        i=0
        for i in range(len(chars)-1):
            print(chars[i],i)
            if chars[i]==chars[i+1]:
                count+=1
            else:
                ap.append(chars[i])
                if count>1 and count<10:
                    ap.append(str(count))
                elif count>=10:
                    # x=len(str(count))
                  for j in str(count):
                      ap.append(j)
                count=1
        print(i,chars[i])
        if len(chars)>1:
            if chars[i]==chars[i+1]:
                ap.append(chars[i])
                if count>1 and count<10:
                        ap.append(str(count))
                elif count>=10:
                    # x=len(str(count))
                    for j in str(count):
                        ap.append(j)
            if chars[i]!=chars[i+1]:
                # print('q')
                # print(chars[i+1],chars[i-1])
                ap.append(chars[i+1])
                # ap.append('1')
            print(ap)
            for i in range(len(ap)):
                chars[i]=ap[i]
            return len(ap)
        else:
            return 1
