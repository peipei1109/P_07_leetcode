# -*- encoding: utf-8 -*-

__author__ = 'luopei'


# Definition for a binary tree node.

#beat 90.48%

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def createTree(self,data):
        
        """
        :type data: list
        :rtype: TreeNode
        """
        
        pass

    
class Solution(object):
    current_max = float('-inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathSumHelper(root)
        return self.current_max

    def maxPathSumHelper(self, root):
        """Helper method"""
        if root is None:
            return root
        left = self.maxPathSumHelper(root.left)
        right = self.maxPathSumHelper(root.right)
        left = 0 if left is None else (left if left > 0 else 0)
        right = 0 if right is None else (right if right > 0 else 0)
        self.current_max = max(left+right+root.val, self.current_max)
        return max(left, right) + root.val
        
        
if __name__=="__main__":
    root=TreeNode(2)
    root.right=TreeNode(-1)
    root.left=TreeNode(1)
    
    obj=Solution()
    print obj.maxPathSum(root)