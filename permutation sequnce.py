from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        a=""
        for i in range(1,n+1):
            a+=str(i)
        perm=[''.join(p) for p in permutations(a)]
        print(perm)
        return perm[k-1]

if __name__=="__main__":
    n,k=map(int,input().split())
    s=Solution().getPermutation(n,k)
    print(s)