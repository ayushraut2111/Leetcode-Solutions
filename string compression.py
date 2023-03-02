# https://leetcode.com/problems/string-compression/
class Solution:
    def compress(self, chars: list[str]) -> int:
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
                  for j in str(count):
                      ap.append(j)
                count=1
        if len(chars)>1:
            if chars[i]==chars[i+1]:
                ap.append(chars[i])
                if count>1 and count<10:
                        ap.append(str(count))
                elif count>=10:
                    for j in str(count):
                        ap.append(j)
            if chars[i]!=chars[i+1]:
                ap.append(chars[i+1])
            for i in range(len(ap)):
                chars[i]=ap[i]
            return len(ap)
        else:
            return 1
