# https://leetcode.com/problems/rotate-list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if head==None or k==0:
            return head
        if head.next==None and k==1:
            return head
        n=0
        temp=head
        prev=temp
        while temp!=None:
            prev=temp
            n+=1
            temp=temp.next
        if k==n:
            return head
        if k>n:
            k-=n*(k//n)
        rot=n-k
        # print(rot)
        prev.next=head
        temp=head
        for i in range(rot):
            temp=head
            head=head.next
        temp.next=None
        return head



        
