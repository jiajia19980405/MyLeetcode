# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        if l1 == None:
            head = l2
        elif l2 == None:
            head = l1
        elif l1!=None and l2!=None :
            if l1.val < l2.val:
                head = ListNode(l1.val)
                l1 = l1.next
            else :
                head = ListNode(l2.val)
                l2 = l2.next
            curr = head
            while l1 != None and l2!= None:
                if l1.val < l2.val:
                    curr.next = l1
                    curr = curr.next
                    l1 = l1.next
                else :
                    curr.next = l2
                    curr = curr.next
                    l2 = l2.next
            if l1 != None:
                curr.next = l1
            else:
                curr.next = l2
        return head



