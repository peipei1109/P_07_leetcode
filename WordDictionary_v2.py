# -*- encoding: utf-8 -*-

__author__ = 'luopei'



# It is not true
import collections
import re
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.word_trie={}
        
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        t=self.word_trie
        for ch in word:
            if ch not in t:
                t[ch]={}
                
            t=t[ch]
        t['#']="#"
                
        
        
                

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        t=self.word_trie;
        
        if not word:
            return False
        if '.' not in word:
            for ch in word:
                if ch not in t: return False
                else: t=t[ch]
            return '#' in t
        
                
        for i, v in enumerate(word):
            if v!='.' and v not in t: return False
            
            if v in t:
                t=t[v]
            if v=='.':
                for k in t:
                    return self.search(word[i+1:])
        
        
            return True

# Your WordDictionary object will be instantiated and called as such:


if __name__=='__main__':
    
    obj = WordDictionary()
    obj.addWord('word')
    print obj.word_trie
    print  obj.search('..rd')