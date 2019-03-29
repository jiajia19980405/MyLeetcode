# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodeMap = {}
        ans = None
        curr = head
        
        while curr!= None:
            if id(curr) not in nodeMap:
                nodeMap[id(curr)] = ''
                curr = curr.next
            else : 
                ans = curr
                break
        return ans