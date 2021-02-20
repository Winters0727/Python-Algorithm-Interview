from collections import defaultdict

class TrieNode:
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        head = self.root
        for char in word:
            head = head.children[char]
        head.word = True
        

    def search(self, word: str) -> bool:
        head = self.root
        for char in word:
            if char not in head.children:
                return False
            head = head.children[char]
        return head.word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        head = self.root
        for char in prefix:
            if char not in head.children:
                return False
            head = head.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)