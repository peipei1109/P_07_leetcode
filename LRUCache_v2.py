# -*- encoding: utf-8 -*-
'''
Created on 2016年10月31日

@author: Administrator

@attention: 这个版本的运行时间得到了优化，通过了所有的case
'''
import heapq
from time import time


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.data = dict()
        self.access = []
        

    def get(self, key):
        """
        :rtype: int
        """
        if not self.data.has_key(key):
            return -1

        (val,_)=self.data[key]
        d_at=time()
        self.data[key]=(val,d_at)

        return self.data[key][0]

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        d_at=time()
        if self.data.has_key(key):
            self.data[key]=(value,d_at)
            return
        
        if self.capacity==0:
            self.remove_lru()
        
        self.data[key]=(value,d_at)
        heapq.heappush(self.access, (d_at,key))
        self.capacity -=1
        
        

    def remove_lru(self):
        while True:
            (lru_at,key)=self.access[0]
            (_,d_at)=self.data[key]
            if d_at>lru_at:
                heapq.heappop(self.access)
                heapq.heappush(self.access, (d_at,key))
                
            else:
                del self.data[key]
                heapq.heappop(self.access)
                self.capacity+=1
                return










