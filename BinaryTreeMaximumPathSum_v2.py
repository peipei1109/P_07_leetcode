
__author__ = 'luopei'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    maxPath = float('-inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.maxPath
    
    
    def dfs(self,node):
        left=right=0 
        if node==None:
            return node           
        if node.left:
            left = self.dfs(node.left)                
            left=max(0,left)
        
        if node.right:
            right=self.dfs(node.right)
            right=max(0,right)
            
        self.maxPath=max(left+right+node.val,self.maxPath)    
        return max(left, right) + node.val
    
if __name__=="__main__":
    root=TreeNode(2)
    root.right=TreeNode(-1)
    root.left=TreeNode(1)
    
    obj=Solution()
    print obj.maxPathSum(root)