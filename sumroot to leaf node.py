# https://leetcode.com/problems/sum-root-to-leaf-numbers
class Solution:
    def sumNumbers(self, root) -> int:
        def treesum(sumr,root):
            if root==None:
                return 0
            sumr=sumr*10+root.val
            if root.left==None and root.right==None:
                return sumr
            x=treesum(sumr,root.left)
            y=treesum(sumr,root.right)
            return x+y
        sumr=0
        return treesum(sumr,root)