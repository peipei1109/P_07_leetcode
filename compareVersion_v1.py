# -*- encoding: utf-8 -*-
'''
Created on 2016年11月1日

@author: Administrator
'''

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1=version1.split(".")
        v2=version2.split(".")
        while v1 and 0==int(v1[-1]): v1.pop()
        while v2 and 0==int(v2[-1]): v2.pop()
        
        print v1, v2
        
        
        for i in xrange(min(len(v1),len(v2))):
            if int(v1[i])==int(v2[i]): continue
            elif int(v1[i])>int(v2[i]): return 1
            elif int(v1[i])<int(v2[i]): return -1
                
        #when len(v1)!=len(v2)
        if len(v1)>len(v2): return 1
        elif len(v1)<len(v2):return -1
        return 0
    
if __name__=="__main__":
    obj=Solution()
    print obj.compareVersion("1.0","1")