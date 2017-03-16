# -*- encoding: utf-8 -*-

__author__ = 'luopei'

import collections
import re
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.word_dic=collections.defaultdict(list)
        
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.word_dic[len(word)].append(word)
                

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dic[len(word)]
        for v in self.word_dic[len(word)]:
            if re.compile(word).match(v):
                return True
        
        
        return False

# Your WordDictionary object will be instantiated and called as such:


if __name__=='__main__':
    
    obj = WordDictionary()
    obj.addWord('word')
    print  obj.search('..rd')