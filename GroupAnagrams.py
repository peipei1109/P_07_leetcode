# -*- encoding: utf-8 -*-
'''
Created on 2016年11月19日

@author: PeiPei
'''
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d=collections.defaultdict(list)
#         d={}
        for i in strs:
            s=''.join(sorted(i))
#             d.setdefault(s,[])
            d[s] +=[i]
        return d.values()
        
            
            

if __name__=="__main__":
    obj=Solution()
    print obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])