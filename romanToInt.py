# -*- encoding: utf-8 -*-
'''
Created on 2016年11月1日

@author: Administrator
'''

d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res, p=0,'I'
        for c in s[::-1]:
            res, p=res-d[c] if d[c]<d[p] else res+d[c], c
        return res
            
            
            

if __name__=="__main__":
    obj=Solution()
    print obj.romanToInt("IV")
    