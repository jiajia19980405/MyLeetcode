# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversd(self,node):
        if node == None:
            return None
        elif node.next == None:
            self.head = node
            return node
        else:
            self.reversd(node.next).next = node
            node.next = None
            return node
    
    def reverseList(self, head):
        #递归
        self.head = None
        self.reversd(head)
        return self.head
    
    
if __name__ == '__main__':
    
    node1 = ListNode(1)
    node2 = node1.next = ListNode(2)
    node3 = node2.next = ListNode(3)

    s = Solution()
    head = s.reverseList(node1)
    while head != None:
        print(head.val)
        head = head.next
    
    