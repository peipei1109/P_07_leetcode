# -*- encoding: utf-8 -*-
'''
Created on 2016年11月1日

@author: Administrator
'''
'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
'''
class Solution(object):
    def combinationSum3(self, k, n):
        return self.solve(k,n,[],1,[])
    
    def solve(self,k,n, so_far,start, ret):
        if(0==k and 0==n):
            ret.append(so_far)
        for i in xrange(start, 10):
            self.solve(k-1, n-i, so_far+[i], i+1, ret)
            
        
        
        return ret    