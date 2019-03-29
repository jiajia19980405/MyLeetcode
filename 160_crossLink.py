# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None :
            return None
        hashmap = {id(headA):headA}
        headA = headA.next
        while headA != None:
            hashmap[id(headA)] = headA
            headA = headA.next
        while headB != None:
            if id(headB) in hashmap :
                return hashmap[id(headB)]
            headB = headB.next
        return None

            