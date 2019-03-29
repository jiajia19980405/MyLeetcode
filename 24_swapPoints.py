# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            former, later = head, head.next
        except:
            return head

        if later == None:
            return head
        head = later
        former.next = later.next
        later.next = former

        while True:
            last = former
            try:
                former = former.next
                later = former.next
            except:
                return head
            if later == None:
                return head
            last.next = later
            former.next = later.next
            later.next = former
