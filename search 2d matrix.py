# https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows=len(matrix)
        columns=len(matrix[0])
        r=0
        c=columns-1
        while r<rows and c>=0:
            mid=matrix[r][c]
            if mid==target:
                return True
            elif mid>target:
                c-=1
            else:
                r+=1
        return False