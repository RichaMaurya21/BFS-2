## Problem 2

#Cousins in binary tree (https://leetcode.com/problems/cousins-in-binary-tree/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousinsBFS(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        q = deque([root])

        while q:
            size = len(q)
            xyList = []           
            for i in range(size):
                current = q.popleft()
                if current.left and current.right:
                    if ((current.left.val == x and current.right.val == y) or (current.left.val == y and current.right.val == x)):
                        return False
                
                if current.left:
                    if current.left.val == x or current.left.val == y:
                        xyList.append(current.left.val)
                    q.append(current.left)

                if current.right:
                    if current.right.val == x or current.right.val == y:
                        xyList.append(current.right.val)
                    q.append(current.right)

            if x in xyList and y in xyList:
                return True

        return False

            
                
class Solution:
    def isCousinsDFS(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        # Initialize variables to keep track of parents and depths
        self.parentX = self.parentY = None
        self.depthX = self.depthY = -1

        # Depth First Search (DFS) helper function
        def dfs(node, parent, level, x, y):
            if not node:
                return
            
            if node.val == x:
                self.parentX, self.depthX = parent, level
            elif node.val == y:
                self.parentY, self.depthY = parent, level
            
            # Continue to search in the left and right children
            dfs(node.left, node, level + 1, x, y)
            dfs(node.right, node, level + 1, x, y)
        
        # Start DFS from the root
        dfs(root, None, 0, x, y)
        
        # Check if x and y are cousins
        return self.depthX == self.depthY and self.parentX != self.parentY