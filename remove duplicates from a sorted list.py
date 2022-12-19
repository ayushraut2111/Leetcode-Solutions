# https://leetcode.com/problems/remove-duplicates-from-sorted-list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if head==None or head.next==None:
            return head
        ptr=head
        temp=head.next
        while temp.next!=None:
            if ptr.val!=temp.val:
                ptr.next=temp
                ptr=temp
            temp=temp.next
        if ptr.val!=temp.val:
            print(ptr.val,temp.val)
            ptr.next=temp
        if ptr.val==temp.val:
            ptr.next=None
        return head

