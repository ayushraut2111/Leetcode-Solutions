# https://leetcode.com/problems/remove-linked-list-elements/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int):
        if head==None:
            return head
        if head.next==None and head.val!=val:
            return head
        if head.next==None and head.val==val:
            return None
        temp=head
        count=0
        while temp!=None:
            if temp.val==val:
                count+=1
                break
            temp=temp.next
        if count==0:
            return head
        while head!=None and head.val==val:
            head=head.next
        if head==None:
            return head
        temp=head
        t1=head
        while temp.next!=None:
            if temp.val==val:
                t1.next=temp.next
                temp=temp.next
                continue
            t1=temp
            temp=temp.next
        if temp.val==val:
            t1.next=None
        return head
        
