# -*- encoding: utf-8 -*-
'''
Created on 2016年11月18日

@author: PeiPei
'''
import collections

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        print sorted(tickets)
        print sorted(tickets)[::-1]
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1] 
    
    
'''
I use a dictionary to represent the tickets (start -> [list of possible destinations]). Then, I start the route at JFK and I dfs from there. Since I do the dfs in sorted order, the first time that I find a possible route, I can return it and know that it is in the smallest lexigraphic order. Finally, note that the worked variable either contains None (as a result of a failed search) or the correct route.
'''

class Solution_2(object):
    def findItinerary(self, tickets):
        d = collections.defaultdict(list)
        for flight in tickets:
            d[flight[0]] += flight[1],
        self.route = ["JFK"]
        def dfs(start = 'JFK'):
            if len(self.route) == len(tickets) + 1:
                return self.route
            myDsts = sorted(d[start])
            for dst in myDsts:
                d[start].remove(dst)
                self.route += dst,
                worked = dfs(dst)
                if worked:
                    return worked
                self.route.pop()
                d[start] += dst,
        return dfs()  


if __name__=="__main__":
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    obj=Solution()
    print  obj.findItinerary(tickets)
    