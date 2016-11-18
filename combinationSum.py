# -*- encoding: utf-8 -*-
'''
Created on 2016年10月31日

@author: Administrator
'''

class Solution(object):
    def __init__(self):
        self.ans=[]
       
    def recursive(self,candidates, target, start, trace):
        if start<len(candidates) and target>=candidates[start]:
            if target>candidates[start]:
                #self.recursive(candidates, target-candidates[start], start+1, trace+[candidates[start]]) #同一个元素不可以重复sum
                self.recursive(candidates, target-candidates[start], start, trace+[candidates[start]]) #同一个元素可以重复sum

            elif target==candidates[start]:
                self.ans.append(trace+[candidates[start]])
            self.recursive(candidates, target, start+1, trace)
    
    def combinationSum(self, candidates, target):
        candidates=sorted(candidates)
        self.recursive(candidates, target, 0, [])
        return self.ans
       

if __name__=="__main__":
    obj=Solution()
    print obj.combinationSum([2,2,3,7],7)