# -*- encoding: utf-8 -*-
'''
Created on 2016年11月17日

@author: Administrator
'''
import bisect
def maxSumSubmatrix(matrix, k):    
    def maxSumSublist(vals):
        maxSum = float('-inf')
        prefixSum = 0
        prefixSums = [float('inf')]
        for val in vals:
            bisect.insort(prefixSums, prefixSum) #将prefixSum插入prefixSums
            prefixSum += val
            i = bisect.bisect_left(prefixSums, prefixSum - k) #返回插入prefixSum - k的位置，但是并不改变orefdixSums           
            maxSum = max(maxSum, prefixSum - prefixSums[i])#prefixSum - prefixSums[i] 是一直小于等于k的~
        return maxSum
        
    maxSum = float('-inf')
    columns = zip(*matrix)
    for left in range(len(columns)):
        rowSums = [0] * len(matrix)
        for column in columns[left:]:
            rowSums = map(int.__add__, rowSums, column)
            print rowSums
            maxSum = max(maxSum, maxSumSublist(rowSums))
    return maxSum

if __name__=="__main__":
    matrix = [[1,  0, 1],[0, -2, 3]]
    k = 2
    obj=maxSumSubmatrix(matrix,k)
    print obj