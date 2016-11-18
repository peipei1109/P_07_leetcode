# -*- encoding: utf-8 -*-
'''
Created on 2016年11月18日

@author: PeiPei
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return  len(nums)!=len(set(nums))

if __name__=="__main__":
    nums=[1,1,2,2,3]
    
    obj=Solution()
    print obj.containsDuplicate(nums)