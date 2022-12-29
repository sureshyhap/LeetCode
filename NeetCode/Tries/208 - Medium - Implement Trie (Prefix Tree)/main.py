class Trie:

    def __init__(self):
        self.end_of_word = False
        self.children = { chr(ord("a") + i) : None for i in range(26) }

    def insert(self, word: str) -> None:
        present = self
        for char in word:
            if not present.children[char]:
                present.children[char] = Trie()
            present = present.children[char]
        present.end_of_word = True

    def search(self, word: str) -> bool:
        present = self
        for char in word:
            if not present.children[char]:
                return False
            present = present.children[char]
        return present.end_of_word

    def startsWith(self, prefix: str) -> bool:
        present = self
        for char in prefix:
            if not present.children[char]:
                return False
            present = present.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
