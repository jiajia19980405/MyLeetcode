class LRUCache:
    #哈希表储存结点的key值为node的引用
    #双向链表储存结点
    #tail为最近使用的
    class Node:
        def __init__(self, key, val):
            self.key = key 
            self.val = val
            self.pre = None
            self.next = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.length = 0
        self.head = None
        self.tail = None
        self.hashmap = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hashmap :
            return -1
        else :
            node = self.hashmap[key]
            ans = node.val
            if node is self.tail:
                return ans

            elif node is self.head:

                self.head = node.next
                self.head.pre = None
                node.pre = self.tail
                self.tail.next = node
                self.tail = node
                node.next = None
                return ans
            else:
                node.pre.next = node.next
                node.next.pre = node.pre
                self.tail.next = node
                node.pre = self.tail
                self.tail = node
                return ans

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        #key值已存在的情况
        if key in self.hashmap :
            node = self.hashmap[key]
            node.val = value
            if node is self.tail :
                return
            elif node is self.head:
                self.head = node.next
                self.head.pre = None
                node.pre = self.tail
                self.tail.next = node
                self.tail = node
                node.next = None
            else:
                node.pre.next = node.next
                node.next.pre = node.pre
                self.tail.next = node
                node.pre = self.tail
                self.tail = node
            return 
        node = self.Node(key, value)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.hashmap[node.key] = node
            self.length += 1

        elif self.length < self.capacity :
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
            self.hashmap[node.key] = node
            self.length += 1

        elif self.length == self.capacity :
            if self.length == 1:
                del self.hashmap[self.head.key]
                self.tail = node
                self.head = node
                self.hashmap[node.key] = node
                return
            else:
                del self.hashmap[self.head.key]
                self.head = self.head.next
                self.tail.next = node
                node.pre = self.tail
                self.tail = node
                self.hashmap[node.key] = node
                return 

            




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1,1)
    lru.put(2,2)
    lru.get(1)
    lru.put(3,3)
    lru.get(2)
    lru.put(4,4)
    lru.get(1)
    lru.get(3)
    lru.get(4)

