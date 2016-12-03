# -*- encoding: utf-8 -*-
'''
Created on 2016年11月1日

@author: Administrator
'''

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if (not board) or len(board[0]) == 0: return 0
        
        visited = [[0 for j in xrange(len(board[0]))] for i in xrange(len(board))]
        ships = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == 'X' and visited[i][j] == 0:
                    ships += 1
                    if i + 1 < len(board) and board[i + 1][j] == 'X' and visited[i + 1][j] == 0:
                        down = i + 1
                        while down < len(board) and board[down][j] == 'X' and visited[down][j] == 0:
                            visited[down][j] = 1
                            down += 1
                    elif j + 1 < len(board[0]) and board[i][j + 1] == 'X' and visited[i][j + 1] == 0:
                        right = j + 1
                        while right < len(board[0]) and board[i][right] == 'X' and visited[i][right] == 0:
                            visited[i][right] = 1
                            right += 1
                visited[i][j] = 1
                    
        return ships
