# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def cmp(self, node):
        return node.val
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        
        j = 0
        while j < length:
            if lists[j] == None:
                del lists[j]
                length -= 1
            else :
                j += 1
        if length == 0:
            return None
        lists.sort(key=self.cmp)
        
        head = lists[0]
        lists[0] = lists[0].next
        if lists[0] == None:
            del lists[0]
            length -= 1
        else:
            i = 0
            while i < length-1 and lists[i].val > lists[i+1].val:
                lists[i], lists[i+1] = lists[i+1], lists[i]
                i += 1
        curr = head

        while length > 0:
            curr.next = lists[0]
            curr = curr.next
            lists[0] = lists[0].next
            if lists[0] == None:
                del lists[0]
                length -= 1
            else:
                i = 0
                while i < length-1 and lists[i].val > lists[i+1].val:
                    lists[i], lists[i+1] = lists[i+1], lists[i]
                    i += 1
        return head
if __name__ == '__main__':
    s = Solution()
    print(s.mergeKLists([None,None]))