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
        left=0;right=length
        
        while(left<=right):
            mid=(left+right)/2
            if citations[mid]==(length-mid):
                return citations[mid]
            elif citations[mid]>(length-mid):right=mid-1
            else:left= mid+1
            
        return length-(right+1)
    
    
    
    
            
        
if __name__=="__main__":
    obj=Solution()
    print obj.hIndex([0,1,3,4,5,5])
    
    