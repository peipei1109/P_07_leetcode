# -*- encoding: utf-8 -*-
'''
Created on 2016年11月1日

@author: Administrator
'''
#有bug， ["XXX"]会输出3 ["XX",".."] 会输出2
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        board=[list(s) for s in board]
        if 0==len(board):
            return 0
        sum=0
        rows=len(board)
        cols=len(board[0])
        if cols==0:
            return 0
        if 1==rows and cols!=0:
            return len(str(board[0]).split(".")) if "X" in board[0] else 0
        for r in xrange(rows):
            for c in xrange(cols):
                if board[r][c]!="X": 
                    continue
                if r==rows-1 or board[r+1][c]!="X":
                    sum +=1
                    if r<rows-1 or not (rows>1 and board[r-1][c]=="X"):
                        while(c<cols and board[r][c]=="X"):
                            c +=1
                    
                
        return sum

if __name__=="__main__":
    board=["X..X","...X","...X"]
    board=[""]
    board=["."]
    obj=Solution()
    sum=obj.countBattleships(board)
    print sum
    