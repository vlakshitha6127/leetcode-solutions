# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s1=[]
        s2=[]
        while l1:
            s1.append(l1.val)
            l1=l1.next
        while l2:
            s2.append(l2.val)
            l2=l2.next
        carry=0
        res=None
        while s1 or s2 or carry:
            v1=s1.pop() if s1 else 0
            v2=s2.pop() if s2 else 0
            total=v1+v2+carry
            carry=total//10
            total=total%10
            node=ListNode(total)
            node.next=res
            res=node
        return res