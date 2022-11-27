# https://leetcode.com/problems/range-sum-query-2d-immutable/
# TLE SOLUTION
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix=matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=0
        for i in range(row1,row2+1):
            print(i)
            # print(sum(self.matrix[i][col1:col2]))
            ans+=sum(self.matrix[i][col1:col2+1])
        return ans