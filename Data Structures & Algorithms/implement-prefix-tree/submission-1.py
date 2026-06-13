class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False

class PrefixTree:

    def __init__(self):
        self.prefixTree = TrieNode()
        

    def insert(self, word: str) -> None:
        trieNode = self.prefixTree.children
        length = len(word)
        for i in range(length):
            if word[i] not in trieNode:
                trieNode[word[i]] = TrieNode()
            if i == length-1:
                trieNode[word[i]].terminal = True
            trieNode = trieNode[word[i]].children
        return


    def search(self, word: str) -> bool:
        trieNode = self.prefixTree.children
        length = len(word)
        for i in range(length):
            if word[i] not in trieNode:
                return False
            elif length-1 == i and trieNode[word[i]].terminal:
                return True
            trieNode = trieNode[word[i]].children
        return False
        

    def startsWith(self, prefix: str) -> bool:
        trieNode = self.prefixTree.children
        length = len(prefix)
        for i in range(length):
            if prefix[i] not in trieNode:
                return False
            elif length-1 == i:
                return True
            trieNode = trieNode[prefix[i]].children
        return False
        
        