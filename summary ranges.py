# https://leetcode.com/problems/summary-ranges/description/
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums)==0:
            return []
        elif len(nums)==1:
            return [str(nums[0])]

        ans=[]
        p=[]
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                p.append(nums[i])
            else:
                p.append(nums[i])
                ans.append(p)
                p=[]
        if nums[-1]!=nums[-2]+1:
            ans.append([nums[-1]])
        else:
            p.append(nums[-1])
            ans.append(p)
        # print(ans)
        t=[]
        for i in ans:
            if len(i)==1:
                t.append(str(i[0]))
            else:
                a=str(i[0])+"->"+str(i[-1])
                t.append(a)
        # print(t)
        return t