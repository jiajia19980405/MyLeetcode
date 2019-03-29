# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addToQue(self,root,k):
        if root == None :
            return
        else :
            self.addToQue(root.left,k)
            if len(self.que) == k :
                return
            self.que.append(root.val)
            self.addToQue(root.right,k)

            
    def kthSmallest(self, root, k):
        self.que = []
        self.addToQue(root,k)
        return self.que[-1]
        
if __name__ == '__main__':
    node = TreeNode(3)
    node1 = node.left = TreeNode(1)
    node2 = node.right = TreeNode(4)
    node3 = node1.right = TreeNode(2)

    s = Solution()
    print(s.kthSmallest(node,1))