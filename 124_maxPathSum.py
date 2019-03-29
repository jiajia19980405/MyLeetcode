# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPath(self,root,nodeMap):
        if root == None:
            return 0
        if id(root) in nodeMap :
            return nodeMap[id(root)]
        else :
            ans = max(self.maxPath(root.left,nodeMap),self.maxPath(root.right,nodeMap),0) + root.val
            nodeMap[id(root)] = ans 
            return ans
    def maxSum(self,root,nodeMap):
        if root == None:
            return 0
        leftAns = self.maxPath(root.left,nodeMap)
        rightAns = self.maxPath(root.right,nodeMap)
        ans = max(leftAns,rightAns,leftAns+rightAns,0) + root.val
        if root.right == None and root.left == None:
            return root.val
        elif root.right == None:
            return max(self.maxSum(root.left,nodeMap),ans)
        elif root.left == None:
            return max(self.maxSum(root.right,nodeMap),ans)
        else :
            return max(self.maxSum(root.left,nodeMap),self.maxSum(root.right,nodeMap),ans)
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #记忆化搜索
        #路径必然是2种情况的一种：
        #1.父节点不为终点
        #2.父节点为终点
        #对于父节点为终点的情况，其最大值为：max(maxPath(root.left),maxPath(root.right)) + root.val
        #对于父节点不为终点的情况，其最大值为：maxPath(root.left) + maxPath(root.right) + root.val
        #为了避免重复运算，应该储存运算结果
        nodeMap = {}
        return self.maxSum(root,nodeMap)

if __name__ == '__main__':
    s = Solution()
    t = TreeNode(2)
    t.left = TreeNode(1)
    t.right = a = TreeNode(2)
    a.left = TreeNode(-1)
    a.right = TreeNode(-2)
    print(s.maxPathSum(t))