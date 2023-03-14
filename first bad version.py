# https://leetcode.com/problems/first-bad-version/
class Solution:
    def firstBadVersion(self, n: int) -> int:
        def isBadVersion(x)->bool:
            pass
        if n<100:
            for i in range(1,n+1):
                if isBadVersion(i)==True:
                    return i
        start=1
        end=n
        while start<=end:
            mid=(end+start+1)//2
            if isBadVersion(mid)==True and isBadVersion(mid-1)==False:
                return mid
            elif isBadVersion(mid)==True:
                end=mid
            else:
                start=mid
            