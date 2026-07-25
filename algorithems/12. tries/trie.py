'''
Trie
'''
class TrieNode:
    '''
    TrieNode
    '''
    def __init__(self):
        self.children = {}  # char → TrieNode
        self.is_end = False  # True if a word ends here

class Trie:
    '''
    Implement trie
    '''
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def get_words_with_prefix(self, prefix: str) -> list[str]:
        """Return all words that start with the given prefix."""
        result = []
        node = self._traverse(prefix)
        
        if not node:
            return result
        
        def _dfs(current_node: TrieNode, current_word: str):
            if current_node.is_end:
                result.append(current_word)
            
            for char, child in current_node.children.items():
                _dfs(child, current_word + char)
        
        _dfs(node, prefix)
        return result

    def count_words_with_prefix(self, prefix: str) -> int:
        """Count number of words with the given prefix."""
        node = self._traverse(prefix)
        
        if not node:
            return 0
        
        def _count(node: TrieNode) -> int:
            total = 1 if node.is_end else 0
            for child in node.children.values():
                total += _count(child)
            return total
        
        return _count(node)

    def search(self, word: str) -> bool:
        """Return True if the word is in the trie."""
        node = self._traverse(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Return True if any word starts with the given prefix."""
        node = self._traverse(prefix)
        return node is not None

    def _traverse(self, prefix: str) -> TrieNode | None:
        """Helper: traverse to the node representing the prefix."""
        node = self.root

        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]

        return node

    def delete(self, word: str) -> bool:
        """Delete a word from the trie and return whether it existed."""
        def _delete(node: TrieNode, depth: int) -> tuple[bool, bool]:
            # Returns:
            # (word_was_deleted, can_delete_this_node)

            if depth == len(word):
                if not node.is_end:
                    return False, False

                node.is_end = False
                return True, len(node.children) == 0

            char = word[depth]

            if char not in node.children:
                return False, False

            child = node.children[char]
            deleted, can_delete_child = _delete(child, depth + 1)

            if can_delete_child:
                del node.children[char]

            can_delete_node = (
                not node.is_end and
                len(node.children) == 0
            )

            return deleted, can_delete_node

        deleted, _ = _delete(self.root, 0)
        return deleted


if __name__ == "__main__":
    word1 = "apple"
    trie = Trie()
    trie.insert(word1)

    word1 = "append"
    trie.insert(word1)

    word1 = "application"
    trie.insert(word1)

    word1 = "appreciate"
    trie.insert(word1)

    print(trie.search("append"))
    print(trie.starts_with("app"))

    print(trie.get_words_with_prefix("app"))
    print(trie.count_words_with_prefix("app"))

    print("----------------------------------------------------------------")
