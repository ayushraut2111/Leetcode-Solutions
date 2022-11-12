# https://leetcode.com/problems/merge-k-sorted-lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertnode(self,root,x):
        if root==None:
            root=ListNode(x)
            # print(root)
            return root
        temp=root
        while temp.next is not None:
            temp=temp.next
        temp.next=ListNode(x)
        return root
    def mergeKLists(self, lists):
        a=[]
        for i in lists:
            temp=i
            while temp is not None:
                a.append(temp.val)
                temp=temp.next
        a.sort()
        root=None
        for i in a:
            root=self.insertnode(root,i)
        return root