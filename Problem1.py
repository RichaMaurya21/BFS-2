# Binary Tree Right Side View (https://leetcode.com/problems/binary-tree-right-side-view/)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #This solution is recursive using dfs, both have O(n) time complexity and space is O(h) where h is height as well as number of leaf nodes
        res = []

        def dfs(node, level):
            if not node:
                return

            if len(res) == level:
                res.append(node.val)

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return res
       #This solution is using BFS
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []
        
        while q:
            size = len(q)
            for i in range(size):
                currNode = q.popleft()
                if i == size - 1:
                    res.append(currNode.val) 
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)

        return res
