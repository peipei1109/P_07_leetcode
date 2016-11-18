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
        j = 0
        for x in nums:
            if x is not 0:
                nums[j] = x
                j += 1
            else:
                pass
        for y in xrange(j,len(nums)):
            nums[y] = 0

        print nums
if __name__=="__main__":
    obj=Solution()
    obj.moveZeroes([0,1,0,3,12,0,1])