# -*- encoding: utf-8 -*-
'''
Created on 2016年10月31日

@author: Administrator
'''

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res =[]
        for i in xrange(1,n+1):
            if 0==i%3 and  0==i%5:
                res.append("FizzBuzz")
            elif 0==i%3:
                res.append("Fizz")
            elif 0==i%5:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
                
            
        
    

if __name__=="__main__":
    obj=Solution()
    print obj.fizzBuzz(15)