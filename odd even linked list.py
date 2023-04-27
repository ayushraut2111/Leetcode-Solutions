# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.root=None
        self.tale=None
    def insert(self,dt):
        if self.root==None:
            self.root=ListNode(dt)
            self.tale=self.root
            return
        self.tale.next=ListNode(dt)
        self.tale=self.tale.next
    def oddEvenList(self, head):
        count=1
        hd=head
        a=[]
        while hd!=None:
            if count%2!=0:
                self.insert(hd.val)
            else:
                a.append(hd.val)
            hd=hd.next
            count+=1
        for i in a:
            self.insert(i)
        return self.root
