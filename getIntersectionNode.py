# -*- encoding: utf-8 -*-
'''
Created on 2016年11月1日

@author: Administrator
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA==None or headB==None:
            return None
        
        nodeSet=()
        nodeSet.add(headA)
        while(headA.next):
            nodeSet.add(headA.next)
            headA=headA.next
        
        while(headB):
            if headB in nodeSet:
                return headB
                