# https://leetcode.com/problems/binary-tree-paths
class Solution:
    def binaryTreePaths(self, root):
        def path(temp,root):
            if root==None:
                return 
            if root.left==None and root.right==None:
                ans.append(''.join(temp)+str(root.val))
                return 
            temp.append(str(root.val)+"->")
            path(temp,root.left)
            path(temp,root.right)
            temp.pop()
        ans=[]
        if root==None:
            return []
        if root.right==None and root.left==None:
            return [str(root.val)]
        path([],root)
        return ans