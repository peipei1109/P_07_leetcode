# -*- encoding: utf-8 -*-
'''
Created on 2016年10月31日

@author: Administrator

@bug: 该版本的效率太低，所以需要用更高效率的改进算法
'''


# -*- encoding: utf-8 -*-
'''
Created on 2016年10月31日

@author: Administrator
'''
from time import *
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        self.val={}
        self.capacity=capacity
        

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.val.keys():
            self.val[key][1]=time()
            return self.val[key][0]
        else:
            return -1
        
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if not self.val.has_key(key):
            if self.capacity>len(self.val.keys()):
                self.val[key]=[]
                self.val[key].extend([value,time()])
#                 print "1", self.val
            else:
                sorted_dic=sorted(self.val.items(), key=lambda x: x[1][1])
                del self.val[sorted_dic[0][0]]
                self.val[key]=[]
                self.val[key].extend([value,time()])
#                 print "2", self.val
            
        else:
            self.val[key]=[value,time()]
#             print "3",self.val      
            
        
        

if __name__=="__main__":
    lru=LRUCache(2)
    lru.set(1,1)
    lru.set(2,2)
    lru.set(3,3)
    lru.set(4,4)
    lru.get(3)
    lru.get(3)
    lru.set(5,5)
    lru.set(5,4)
    lru.get(1)
    
    