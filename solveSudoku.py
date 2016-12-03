# -*- encoding: utf-8 -*-
'''
Created on 2016年11月1日

@author: Administrator
'''

#Maintain hashsets for each row, column and block, then at each '.', using the valid numbers to do dfs, if cannot make it, back track.

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return 
        global colM, rowM, blockM
        colM, rowM, blockM= [set() for c in xrange(9)], [set() for c in xrange(9)], [set() for c in xrange(9)]
        for r in xrange(9):
            for c in xrange(9):
                v = board[r][c]
                if v!='.':
                    v=int(v)
                    block = (r/3)*3+c/3
                    colM[c].add(v)
                    rowM[r].add(v)
                    blockM[block].add(v)
        def solve(r,c):
            global colM, rowM, blockM
            if board[r][c]!='.': # if this case is filled 
                if r==8 and c==8: return True
                return solve(r+(c+1)/9, (c+1)%9)
            else: # do dfs 
                for v in xrange(1,10):
                    if v not in colM[c] and v not in rowM[r] and v not in blockM[(r/3)*3+c/3]:
                        colM[c].add(v)
                        rowM[r].add(v)
                        blockM[(r/3)*3+c/3].add(v)
                        board[r][c]=str(v)
                        if solve(r,c)==False: # dfs
                            colM[c].discard(v)
                            rowM[r].discard(v)
                            blockM[(r/3)*3+c/3].discard(v) # backtracking
                            board[r][c]='.'
                        else: return True
                return False
        print solve(0,0)


if __name__=="__main__":
    pass