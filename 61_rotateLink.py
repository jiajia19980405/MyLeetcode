
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        count = 0
        
        end = head
        while end != None:
            end = end.next
            count += 1
        k = k % count
        if k == 0:
            return head
        end = head
        aim = head
        pre = None
        for i in range(k-1):
            end = end.next
        while end.next != None:
            end = end.next
            pre = aim
            aim = aim.next
        end.next = head
        head = aim
        pre.next = None
        return head 


if __name__ == '__main__':
    head = ListNode(1)
    curr = head
    for i in range(2,3):
        curr.next = ListNode(i)

    s = Solution()
    print(s.rotateRight(head,0))
    