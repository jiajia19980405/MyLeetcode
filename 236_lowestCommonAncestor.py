# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ans = None
    def lowestCommonAncestor(self, root, p, q):
        if root == None :
            return root
        if (root is p) or (root is q):
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        sset = [left,right,root]

        if (p in sset) and (q in sset) :
            self.ans = root
            return root
        elif p in sset :
            return p
        elif q in sset :
            return q
        else:
            return self.ans

if __name__ == '__main__':
    node1 = TreeNode(-1)
    node2 = node1.left = TreeNode(0)
    node3 = node1.right = TreeNode(3)
    node4 = node2.left = TreeNode(-2)
    node5 = node2.right = TreeNode(4)
    node6 = node4.left = TreeNode(8)
    # node6 = node5.right = TreeNode(4)
    # node3.left = TreeNode(0)
    # node3.right = TreeNode(8)

    s = Solution()

    print(s.lowestCommonAncestor(node1,node5,node6).val)