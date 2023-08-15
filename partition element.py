# https://leetcode.com/problems/partition-list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x: int):
        if head==None or head.next==None:
            return head
        temp=head
        a=[]
        b=[]
        while temp!=None:
            if temp.val<x:
                a.append(temp)
            else:
                b.append(temp)
            temp=temp.next
        if a==[]:
            return head
        if b==[]:
            return head
        for i in range(len(a)-1):
            a[i].next=a[i+1]
        a[-1].next=b[0]
        for i in range(len(b)-1):
            b[i].next=b[i+1]
        b[-1].next=None
        return a[0]

        
        