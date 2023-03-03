# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            if target-numbers[i] in numbers[i+1:]:
                return [i+1,numbers[i+1:].index(target-numbers[i])+i+2]