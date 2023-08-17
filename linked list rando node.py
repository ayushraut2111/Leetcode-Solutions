# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/linked-list-random-node
import random
class Solution:

    def __init__(self, head):
        self.ls=[]
        temp=head
        while temp!=None:
            self.ls.append(temp.val)
            temp=temp.next
        

    def getRandom(self) -> int:
        return random.choice(self.ls)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()