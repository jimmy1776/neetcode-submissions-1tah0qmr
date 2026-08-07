#Claude's version
# The trick is that the entire tree is nothing but dictionaries inside dictionaries. 
# Every key is a single letter pointing at another dictionary. 
# TLDR: Three methods walking nested dicts, one letter per step.

class PrefixTree:

    def __init__(self):
        self.root = {}

    
    def insert(self, word :str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['*'] = True 


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '*' in cur
    
    def startsWith(self,prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur:
                return False 
            cur = cur[c]
        return True 
    

    

        
    





















