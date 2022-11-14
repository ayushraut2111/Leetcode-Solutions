class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        st={}
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if (nums[i]+nums[j]) not in st:
                    st[nums[i]+nums[j]]=[[nums[i],nums[j]]]
                else:
                    st[nums[i]+nums[j]].append([nums[i],nums[j]])
        ans=[]
        for i in nums:
            if -i in st:
                x=[i]
                x.append(st[-i])
                ans.append(x)
        print(ans)

s=Solution()
nums=list(map(int,input().split()))
print(s.threeSum(nums)) 
#not fully solved 