# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/remove-nth-node-from-end-of-list
class Solution:
    def removeNthFromEnd(self, head, n: int):
        temp=head
        count=0
        while temp!=None:
            temp=temp.next
            count+=1
        x=count
        count-=n
        if count==0:
            head=head.next
            return head
        temp=head
        curr=temp
        for i in range(count):
            curr=temp
            temp=temp.next
        if temp.next is not None:
            curr.next=temp.next
        else:
            curr.next=None
        return head