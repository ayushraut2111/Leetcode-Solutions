# https://leetcode.com/problems/reverse-linked-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        if head==None or head.next==None:
            return head
        prev=None
        curr=None
        Nex=None
        curr=head
        while curr!=None:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        return prev