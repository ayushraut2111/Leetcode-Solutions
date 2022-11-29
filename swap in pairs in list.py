# https://leetcode.com/problems/swap-nodes-in-pairs
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        if head==None or head.next==None:
            return head
        x=head
        head=head.next
        ptr=head.next
        head.next=x
        c=self.swapPairs(ptr)
        x.next=c
        return head