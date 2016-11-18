# -*- encoding: utf-8 -*-
'''
Created on 2016年10月31日

@author: Administrator
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda v: v == 0)
        print nums

if __name__=="__main__":
    obj=Solution()
    obj.moveZeroes([0,1,0,3,12,0,1])
    