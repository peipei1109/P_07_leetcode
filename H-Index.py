# -*- encoding: utf-8 -*-

__author__ = 'luopei'

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations=sorted(citations)
        length=len(citations)
        mid=length/2
        current_h=0
        if citations[mid]>=length-mid:
            current_h=length-mid
            
            for i in xrange(mid-1,0,-1):   #此处可以改成二叉查找 ,提高查询效率
                if citations[i]>=(length-i):current_h=length-i
                else: break
        else:             
            for i in xrange(mid+1,length): #此处可以改成二叉查找 ,提高查询效率               
                if  citations[i]>=(length-i):
                    current_h=length-i
                    break        
            
        return current_h
        
if __name__=="__main__":
    obj=Solution()
    print obj.hIndex([0,2,1,1,1])
    
    