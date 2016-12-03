# -*- encoding: utf-8 -*-
'''
Created on 2016年11月1日

@author: Administrator
'''

# the performace is bad than v1
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        def encode(version):
            vals = [long(v) for v in version.split(".")]
            while vals and vals[-1] == 0: # get rid of trailing 0s in the array
                vals.pop()
            return vals
        return cmp(encode(version1), encode(version2)) # default comparison of two arrays
    
    
    