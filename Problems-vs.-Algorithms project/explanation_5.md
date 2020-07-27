# Autocomplete with Tries

technically all operations in a dictionary can take O(n) in worst case because of collisions but in practice it's almost imposible, so that's why we'll use O(1) the avg. case,
Given a "root" node, the solution recursively loops through all of the node's children. Whenever a "word" node is encountered, it is added to the list of suffixes.

# TrieNode:
our TrieNode needs to state wether it's a word end, and have a dictionary of children TrieNodes.

# Efficiency
insert: time complexity is O(1), space complexity is O(1)
suffixes: time complexity O(P\*Q) where P is the number of children per Node, while Q is the depth of the Trie tree
space complexity: O(P\*Q) with P being the length of a word , and Q the Number of words in the tree.

# Trie:
a Trie has a root TrieNode, with insert and find functions A

# Efficiency
insert: time complexity O(n), space complexity O(n)
find: time complexity O(n) where n is the length of the prefix and space complexity is O(1)
