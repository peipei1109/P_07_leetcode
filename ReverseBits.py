# -*- encoding: utf-8 -*-
'''
Created on 2016年11月19日

@author: PeiPei
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = bin(n)[2:]
        s = '0' * (32-len(s)) + s
#         s = bin(n)[2:].zfill(32)
        num = int(s[::-1], 2)
        return num


if __name__=="__main__":
    obj=Solution()
    print obj.reverseBits(43261596)