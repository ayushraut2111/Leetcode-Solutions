# https://leetcode.com/problems/insertion-sort-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.xy=None
    def insertnode(self,i,ptr):
        t=ListNode(i)
        if self.xy==None:
            self.xy=t
            return self.xy
        ptr.next=t
        return ptr.next
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
        return self.xy