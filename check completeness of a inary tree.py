# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def height(self,root):
        if root==None:
            return 0
        x=self.height(root.left)
        y=self.height(root.right)
        return max(x,y)+1
    def isCompleteTree(self, root):
        if root==None or (root.left==None and root.right==None):
            return True
        q=[]
        q.append(root)
        i=0
        h=self.height(root)
        print(h)
        while len(q)!=0:
            if i!=h-1 and len(q)<2**i:
                return False
            if i!=h-2:
                n=len(q)
                for j in range(n):
                    a=q.pop(0)
                    if a.left!=None:
                        q.append(a.left)
                    if a.right!=None:
                        q.append(a.right)
            else:
                x=len(q)
                for j in range(x):
                    a=q.pop(0)
                    if a.left==None and a.right!=None:
                        return False
                    if a.left!=None and a.right==None:
                        if j!=x-1:
                            for k in range(j,x-1):
                                z=q.pop(0)
                                if z.left!=None or z.right!=None:
                                    return False
                            return True
                        else:
                            return True
                        # return False
                    if a.left==None and a.right==None:
                        if j!=x-1:
                            for k in range(j,x-1):
                                z=q.pop(0)
                                if z.left!=None or z.right!=None:
                                    return False
                            return True

                    if a.left!=None:
                        q.append(a.left)
                    if a.right!=None:
                        q.append(a.right)
            i+=1
        return True
        