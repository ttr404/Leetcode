# ---------- clone_graph_bfs.py ----------

from collections import deque
from typing import Optional

class Node:
    def __init__(self, val: int = 0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph_BFS(node: Optional[Node]) -> Optional[Node]:
    """
    Deep-copies a connected undirected graph using queue (BFS).
    """
    if node is None:
        return None

    # Map original node → cloned node
    old_to_new = {node: Node(node.val)}
    q = deque([node])

    while q:
        cur = q.popleft()

        for nei in cur.neighbors:
            if nei not in old_to_new:
                # clone this unseen neighbor
                old_to_new[nei] = Node(nei.val)
                q.append(nei)

            # connect the clone of current to the clone of neighbor
            old_to_new[cur].neighbors.append(old_to_new[nei])

    return old_to_new[node]


class Solution(object):
    def cloneGraph(self, node):
        if node is None:
            return None

        old_to_new = {}

        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]

            clone = Node(curr.val)
            old_to_new[curr] = clone
            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node)

