# -*- encoding: utf-8 -*-
'''
Created on 2016年11月1日

@author: Administrator
'''
class Solution(object):
    def combinationSum3(self, k, n):
        if k <= 0 or n < 1: return []
        res = []
        def dfscom(kk, nn, ares):
            if 0 == kk: 
                if nn == 0: res.append(ares)
                return
            startn = ares[-1] + 1 if ares else 1
            div1, div2 = 2*nn+kk-kk*kk, 2*kk
            endn = min(11-kk, div1/div2 + 1)
            for i in range(startn, endn):
                dfscom(kk-1, nn-i, ares + [i])
        dfscom(k, n, [])
        return res

if __name__=="__main__":
    pass