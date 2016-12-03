# -*- encoding: utf-8 -*-
'''
Created on 2016年10月31日

@author: Administrator
'''

import random
import collections

#插入删除什么的都在O(1)
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values, self.idxs=[], collections.defaultdict(set)
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        self.values.append(val)
        self.idxs[val].add(len(self.values)-1)
        return 1==len(self.idxs[val])
        
        
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.idxs[val]:
            out, ins=self.idxs[val].pop(),self.values[-1]
            self.values[out]=ins
            self.idxs[ins].add(out)
            self.idxs[ins].discard(len(self.values)-1)
            self.values.pop()
            return True
        return False
    
    
    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: in
        """
        if 0<len(self.values):
            return random.choice(self.values)
        
        else:
            return -1
       
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


if __name__=="__main__":
    obj = RandomizedCollection()
    param_1 = obj.insert(1)
    param_2 = obj.remove(1)
    param_3 = obj.getRandom()