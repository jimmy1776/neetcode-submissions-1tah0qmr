class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["$"] = True

    
    def search(self,word: str) -> bool:
        def dfs(j,node):
            cur = node 
            for i in range(j,len(word)):
                c = word[i]
                if c == ".":
                    for child in cur:
                        if child != "$" and dfs(i +1, cur[child]):
                            return True 
                    
                    return False 
                else:
                    if c not in cur:
                        return False 
                    
                    cur = cur[c]
            return "$" in cur 
        
        return dfs(0,self.root)