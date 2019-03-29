# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        if head == None:
            return None
        else:
            return self.mergeSort(head)
    
    def mergeSort(self, head):
        if head == None or head.next == None:
            return head
        mid = head
        quick, slow = head, head
        while quick != None and quick.next != None :
            mid = slow
            quick = quick.next.next
            slow = slow.next
        
        mid.next = None

        l = self.mergeSort(head)
        r = self.mergeSort(slow)

        return self.merge(l,r)
    
    def merge(self,l,r):
        head = None
        curr = head
        while l != None and r != None:
            temp = None
            if l.val < r.val:
                temp = l
                l = l.next
            else:
                temp = r
                r = r.next
            if head == None:
                head = temp
                curr = head
            else:
                curr.next = temp
                curr = curr.next
        if l != None:
            curr.next = l
        else:
            curr.next = r
        return head

if __name__ == '__main__':
    node1 = ListNode(4)
    node2 = node1.next = ListNode(2)
    node3 = node2.next = ListNode(1)
    node4 = node3.next = ListNode(3)

    s = Solution()
    head = s.sortList(node1)

    while head != None:
        print (head.val)
        head = head.next
