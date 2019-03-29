# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        curr = head
        former = None
        for i in range(n):
            temp = temp.next
        while temp != None :
            temp = temp.next
            former = curr
            curr = curr.next
        if former == None:
            head = head.next
        else:
            former.next = curr.next
        return head
            