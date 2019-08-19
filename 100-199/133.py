"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
# https://leetcode-cn.com/problems/clone-graph/solution/dfs-he-bfs-by-powcai/

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        lookup = {}

        def dfs(node):
            if not node:
                return
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone

        return dfs(node)


from collections import deque


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        lookup = {}

        def bfs(node):
            if not node:
                return
            clone = Node(node.val, [])
            lookup[node] = clone
            queue = deque()
            queue.append(node)
            while queue:
                tmp = queue.pop()
                for n in tmp.neighbors:
                    if n not in lookup:
                        lookup[n] = Node(n.val, [])
                        queue.appendleft(n)
                    lookup[tmp].neighbors.append(lookup[n])
            return clone

        return bfs(node)