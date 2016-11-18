# -*- encoding: utf-8 -*-
'''
Created on 2016年11月1日

@author: Administrator
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        level=[root]
        reverse=False
        res=[]
        while level:
            if reverse: res.append([node.val for node in level[::-1]])
            else:res.append([node.val for node in level])
            pairs=[(node.left, node.right) for node in level]
            level=[node for pair in pairs for node in pair if node]
            reverse = not reverse            
            
        return res   

if __name__=="__main__":
    obj=Solution()
#     obj.zigzagLevelOrder(root)