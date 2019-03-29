# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #两个指针，一个指向k个节点链表的第一个节点，一个指向k个链表的最后一个节点
        #将这个链表反转
        #再接到原链表上
        if k == 1:
            return head
        if k == 2:
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
        leader = None
        first = head
        while True:
            last = first
            try:
                for i in range(k-1):
                    last = last.next
            except:
                return head
            if last == None:
                return head
            a,b,c = first, first.next, first.next.next
            while c != last and c != None:
                b.next = a
                a = b
                b = c
                c = c.next
            
            if leader == None:
                head = last
            else:
                leader.next = last
            leader = first
            first.next = c.next
            first = c.next
            c.next = b
            b.next = a


                