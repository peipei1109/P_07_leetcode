# -*- encoding: utf-8 -*-

__author__ = 'luopei'


import copy
res=[]
results=[[]]
class Solution(object):
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        return self.Ck(nums, len(nums))
        
    
    #有bug，没有去掉重复的set
    def Ck(self,nums, k):
                
        
        if k==0:
            return [[]]
        
        for subset in self.Ck(nums, k-1):

            num_list=copy.deepcopy(nums)
            for elem in subset:
                num_list.remove(elem)
    
            for num in num_list:
                sub_list=copy.deepcopy(subset)
                sub_list.append(num)
                res.append(sub_list)
        for r in res:
            if list(set(r)) not in results:
                results.append(list(set(r)))
        return results
        
        
    # DFS recursively 
    def subsets1(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
        
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
            
    # Bit Manipulation    
    def subsets2(self, nums):
        res = []
        nums.sort()
        for i in xrange(1<<len(nums)):
            tmp = []
            for j in xrange(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
        
    # Iteratively
    def subsets3(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res
        
            
if __name__=="__main__":
    
    obj=Solution()
    print obj.subsets([1,2,3])