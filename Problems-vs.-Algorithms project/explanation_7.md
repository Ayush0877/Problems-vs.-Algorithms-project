# HTTPRouter using a Trie

Technically, all operations in a dectionary can take O(n) in worst case because of collisions but in practice it's almost imposible, so that's why we'll use O(1) as the avg. case.

# RouteTrieNode:

our RouteTrieNode has a children dictionary and a handler

# Efficiency

insert: time complexity is O(1), space complexity is O(n), where n is the length of the route.

# RouteTrie:

a RouteTrie has a root RouteTrieNode, with insert and find functions

# Efficiency

insert: time complexity O(n), space complexity O(n)
find: time complexity O(P\*Q) where Q is the length of the part of the route, P is the depth of the route and space complexity: O(1)

# Router:

a Router has a root RouteTrie, with add_handler and lookup and split_path functions

# Efficiency

add handler: time complexity is O(n), space complexity is O(n)
lookup: is efficiency of the RouteTrie find function.
split_path: time complexity is O(n), space complexity is O(n)

# The `add_handler` method #
The `add_handler` method splits a given path (`/a/b/c`, for example) into a list of segments (`['a', 'b', 'c']`). This gives the `add_handler` method a space efficiency of `O(n)`, where `n` is the number of segments in the path.

For example, in the following code, `n` is 3:

```python
router = Router()
router.add_handler('/a/b/c', 'Handler')
```
