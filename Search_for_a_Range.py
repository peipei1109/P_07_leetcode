# -*- encoding: utf-8 -*-
'''
Created on 2016年11月19日

@author: PeiPei
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = self.binarySearch(0, len(nums)-1,nums, target) 
        if i == -1:
            return [i, i]
        j, k = i, i
        while j >= 0:
            j1 = j
            j = self.binarySearch(0, j1-1, nums, target)
        while k >= 0:
            k1 = k
            k = self.binarySearch(k1+1, len(nums)-1, nums, target)
        return [j1, k1]
    
    def binarySearch(self, begin, end, nums, target):
        if begin > end:
            return -1
        mid = (begin+end)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(mid+1, end, nums, target)
        else:
            return self.binarySearch(begin, mid-1, nums, target)

if __name__=="__main__":
    nums=[5, 7, 7, 8, 8, 10]
    obj=Solution()
    print obj.searchRange(nums,8)
    