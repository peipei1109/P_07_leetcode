# -*- encoding: utf-8 -*-
'''
Created on 2016年11月17日

@author: Administrator
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        def dfs(root, left=False):
            if not root: return 0
            if left and root.left is root.right: 
                return root.val
            return dfs(root.left, True) + dfs(root.right)
        return dfs(root)

if __name__=="__main__":
    tree=TreeNode(3)
    tree.left=TreeNode(9)
    tree.right=TreeNode(20)
    tree.right.left=TreeNode(15)
    tree.right.right=TreeNode(7)
    obj=Solution()
    print obj.sumOfLeftLeaves(tree)
    
    