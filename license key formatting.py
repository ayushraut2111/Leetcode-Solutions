# https://leetcode.com/problems/license-key-formatting/
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.upper()
        a=[]
        for i in s:
            if i!='-':
                a.append(i)
        st=""
        if len(a)%k!=0:
            st=st.join(a[:len(a)%k])
            st+='-'
            a=a[len(a)%k:]
        for i in range(0,len(a),k):
            x=''.join(a[i:i+k])
            st+=x+'-'
        return st[0:len(st)-1]

        
        