# -*- encoding: utf-8 -*-

__author__ = 'luopei'

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations)==0:
            return 0
        citations=sorted(citations)
        length=len(citations)
        left=0;right=length-1 #这里要为length-1，否则，当citations 里面全是0时会出现Index out of range
        
        while(left<=right):
            mid=(left+right)/2
            if citations[mid]==(length-mid):
                return citations[mid]
            elif citations[mid]>(length-mid):right=mid-1
            else:left= mid+1
            
        return length-(right+1)
    
    
    
    
            
        
if __name__=="__main__":
    obj=Solution()
    print obj.hIndex([0,1,2,3,5,5])
    
    