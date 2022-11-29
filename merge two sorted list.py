# https://leetcode.com/problems/merge-two-sorted-lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1==None and list2==None:
            return None
        if list1==None:
            return list2
        if list2==None:
            return list1
        tail=ListNode(0)
        px=tail
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                px.next=list1
                list1=list1.next
            else:
                px.next=list2
                list2=list2.next
            px=px.next
        while list1!=None:
            px.next=list1
            list1=list1.next
            px=px.next
        while list2!=None:
            px.next=list2
            list2=list2.next
            px=px.next
        tail=tail.next
        return tail

        
        