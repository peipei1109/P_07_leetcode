# -*- encoding: utf-8 -*-
'''
Created on 2016年11月17日

@author: Administrator
'''

#Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.
'''
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?

'''

#beat 98.90%，但是没看懂呀

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        M, N = min(m,n), max(m,n)
        ans = None
        def findMaxArea(sums, beg, end):
            if beg + 1 >= end: return None
            mid = beg + ((end - beg)>>1)
            res = max(findMaxArea(sums, beg, mid), findMaxArea(sums, mid, end))
            i = mid
            for l in sums[beg:mid]:
                while i < len(sums) and sums[i] - l <= k:
                    res = max(res, sums[i] - l)
                    i += 1
            sums[beg:end] = sorted(sums[beg:end])
            return res

        for i1 in xrange(M):
            tmp = [0]*N
            for i2 in xrange(i1, M):
                sums, low, maxArea = [0], 0, None
                for j in xrange(N):
                    tmp[j] += matrix[i2][j] if m <= n else matrix[j][i2] #当前遍历的行的j列的和
                    print "tmp:",tmp[j]
                    sums.append(sums[-1] + tmp[j])
                    print "sums:",sums, i1,i2, j
                    maxArea = max(maxArea, sums[-1] - low)
                    low = min(low, sums[-1])
                    print low,maxArea
                if maxArea <= ans: continue
                if maxArea == k: return k
                if maxArea > k: maxArea = findMaxArea(sums, 0, N+1)
                ans = max(ans, maxArea)
        return ans or 0
        
        
        
        
        
if __name__=="__main__":
    matrix = [[1,  0, 0],[0, -2, 3]]
    k = 2
    obj=Solution()
    sum=obj.maxSumSubmatrix(matrix, k)
    print sum
    