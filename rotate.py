# -*- encoding: utf-8 -*-
'''
Created on 2016年10月31日

@author: Administrator
'''

class Solution(object):
    def rotate(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in xrange(len(m) / 2 + len(m) % 2):
            for j in xrange(len(m) / 2):
                m[i][j], m[-1-j][i], m[-1-i][-1-j], m[j][-1-i] = m[-1-j][i], m[-1-i][-1-j], m[j][-1-i], m[i][j]


if __name__=="__main__":
    pass