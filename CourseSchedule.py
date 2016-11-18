# -*- encoding: utf-8 -*-
'''
Created on 2016年11月18日

@author: PeiPei
'''
    
'''
if node v has not been visited, then mark it as 0.
if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.
'''  
class Solution_1(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        for x, y in prerequisites:
            print x,y
            graph[x].append(y)
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        for i in xrange(numCourses):
            if not dfs(i):
                return False
        return True

#Could be cleaner code. Check this out.
class Solution_2(object):
    def canFinish(self, n, edges):
        graph = {i:set() for i in range(n)}
        indeg = {i:0     for i in range(n)}
        for s, e in set(tuple(x) for x in edges):
            graph[s] |= {e}
            indeg[e] += 1
        queue  =  [i for i in range(n) if not indeg[i]]
        visits =  set(queue) 
        for node in queue:
            for neigh in graph[node]:
                if neigh in visits: 
                    return False
                indeg[neigh] -= 1
                if not indeg[neigh]:
                    visits.add(neigh)
                    queue += neigh,
        return len(visits) == n
    
    

#This solution might be longer, but it is slightly easier to read. Comments are in-line. Thanks.

class Solution_3(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        # create graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        # visit each node
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        # mark as being visited
        visited[i] = -1
        # visit all the neighbours
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        return True
    
    
import collections

'''
This solution is similar to others posted using BFS with an improvement. To speed up removal of outgoing edges I create an edgemap to look up outgoing edges without having to loop thru vertices or edges over and over again. I believe time complexity would be O(V+E).
'''   
class Solution_4(object):
    def canFinish(self, numCourses, prereqs):
        inCount = [0 for i in range(numCourses)]
        edgemap = {i: [] for i in range(numCourses)}
        for e in prereqs:
            inCount[e[1]] += 1
            edgemap[e[0]].append(e[1])
        # Add courses with no prereqs to queue
        q = collections.deque(i for i in range(numCourses) if inCount[i]==0)
        count = 0
        while q:
            node = q.popleft()
            count += 1
            # Remove all outgoing edges
            for out in edgemap[node]:
                inCount[out] -= 1
                if inCount[out] == 0:
                    q.append(out)
        return count == numCourses 
    
    
    
if __name__=="__main__":
    numCourses=2
    prerequisites=[[1,0],[0,1]]
    obj=Solution_1()
    obj.canFinish(numCourses, prerequisites)