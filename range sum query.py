# https://leetcode.com/problems/range-sum-query-immutable
class NumArray:

    def __init__(self, nums: list[int]):
        self.nums=nums
        self.n=len(nums)
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])