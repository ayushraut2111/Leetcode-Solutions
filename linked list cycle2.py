#https://leetcode.com/problems/linked-list-cycle-ii/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        a=[]
        temp=head
        while temp is not None:
            if temp in a:
                return temp
            a.append(temp)
            temp=temp.next
        return None
