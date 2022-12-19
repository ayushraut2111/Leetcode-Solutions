# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if head==None or head.next==None:
            return head
        if left==1 and right==1:
            return head
        temp=head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next
        if right-left+1==count:
            prev=None
            curr=head
            nex=None
            while curr!=None:
                nex=curr.next
                curr.next=prev
                prev=curr
                curr=nex
            return prev
        i=1
        temp=head
        t1=head
        while temp.next!=None and i<left:
            t1=temp
            i+=1
            temp=temp.next
        io=head
        j=1
        while io.next!=None and j<right:
            j+=1
            io=io.next
        print(t1.val,io.val)
        prev=io.next
        curr=temp
        nex=curr
        print(t1.val,io.val)
        while curr!=None and i-1<j:
            # print(curr.val,i)
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
            i+=1
        # print(curr.val)
        if left==1:
            return prev
        t1.next=prev
        return head
        