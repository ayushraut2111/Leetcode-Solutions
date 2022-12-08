# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.root=None
    def insert(self,i,head):
        ptr=ListNode(i)
        if self.root==None:
            self.root=ptr
            return self.root
        head.next=ptr
        return head.next
    def deleteDuplicates(self, head):
        temp=head
        dict={}
        while temp is not None:
            if temp.val not in dict:
                dict[temp.val]=1
            else:
                dict[temp.val]+=1
            temp=temp.next
        a=[]
        for key,value in dict.items():
            if value>1:
                a.append(key)
        for i in a:
            del dict[i]
        # print(dict)
        a=[]
        for i in dict.keys():
            a.append(i)
        h=None
        for i in a:
            h=self.insert(i,h)
        return self.root
        