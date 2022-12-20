# https://leetcode.com/problems/find-mode-in-binary-search-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root) -> list[int]:
        if root==None:
            return []
        if root.left==None and root.right==None:
            return [root.val]
        
        queue=[]
        dic={}
        queue=[root]
        while len(queue)>0:
            x=queue.pop(0)
            if x.val in dic:
                dic[x.val]+=1
            else:
                dic[x.val]=1
            if x.left!=None:
                queue.append(x.left)
            if x.right!=None:
                queue.append(x.right)
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        x=dic[0][1]
        ans=[]
        for i in dic:
            if i[1]==x:
                ans.append(i[0])
        print(ans)
        return ans
