# -*- encoding: utf-8 -*-
'''
Created on 2016年11月1日

@author: Administrator
'''



class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        visited = { (0,0) : True}
        candidates = [(0,0)]
        def add_candidate(candidate):
            if candidate not in visited:
                visited[candidate] = True
                candidates.append(candidate)
        index = 0
        while index < len(candidates):
            c = candidates[index]
            index += 1
            if c[0] + c[1] < len(s3):
                nextchar = s3[c[0] + c[1]]
                if c[0] < len(s1) and nextchar == s1[c[0]]:
                    add_candidate( (c[0]+1, c[1]) )
                if c[1] < len(s2) and nextchar == s2[c[1]]:
                    add_candidate( (c[0], c[1]+1) )
        return (len(s1), len(s2)) in visited
    
    
    
if __name__=="__main__":
    obj=Solution()
    sum=obj.isInterleave("a","b","ab")
    print sum