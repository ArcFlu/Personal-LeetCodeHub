"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        nodeMap = {}
        
        def DFS(currNode):  
            retNode = Node(currNode.val)
            nodeMap[currNode.val] = retNode
            
            for n in currNode.neighbors:
                if n.val not in nodeMap:
                    retNode.neighbors.append(DFS(n))
                else:
                    retNode.neighbors.append(nodeMap[n.val])
            return retNode
        return DFS(node)
                