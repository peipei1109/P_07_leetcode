# -*- encoding: utf-8 -*-

__author__ = 'luopei'




# Time Limit Exceeded。。。。。。。
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        results=[]
        for i, num in enumerate(nums):
            count=0;
            for rest_num in nums[i+1:]:
                if  rest_num< num:
                    count =count+1
            results.append(count)
        return results

if __name__=="__main__":
    obj=Solution()
    print obj.countSmaller([5, 2, 6, 1])