# https://leetcode.com/problems/insertion-sort-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertnode(self,i,ptr):
        t=ListNode(i)
        if ptr==None:
            ptr=t
            return ptr
        temp=ptr
        while temp.next is not None:
            temp=temp.next
        temp.next=t
        return ptr
    def insertionSortList(self, head):
        temp=head
        a=[]
        while temp is not None:
            a.append(temp.val)
            temp=temp.next
        ptr=None
        a.sort()
        for i in a:
           ptr=self.insertnode(i,ptr)
        return ptr


