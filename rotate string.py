# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, b: str, a: str) -> bool:
        temp=a*2
        if len(a)<len(b):
            return False
        for i in range(len(temp)-len(b)+1):
            if temp[i]==b[0]:
                k=0
                count=0
                for j in range(i,i+len(b)):
                    if temp[j]==b[k]:
                        count+=1
                        k+=1
                    else:
                        break
                if count==len(b):
                    return True