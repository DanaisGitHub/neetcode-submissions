
class TrieNode:
    def __init__(self): # no value actually sotred in the node, as the key,value the key is character
        self.children = {} 
        self.word = False # end of the word or not
        
class PrefixTree:

    def __init__(self):
        self.root =  TrieNode() # {children, word}

    def insert(self, word: str) -> None:
        currNode = self.root
        self.root.children
        for c in word:
            if c not in currNode.children:
                currNode.children[c] = TrieNode()
            currNode = currNode.children[c]
        currNode.word = True

    def search(self, word: str) -> bool:
        currNode = self.root
        for c in word:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        return currNode.word
        
    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for c in prefix:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        return True

