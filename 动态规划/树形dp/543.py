from typing import List, Optional
# https://leetcode.cn/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            if node is None:
                return -1
            
            l = dfs(node.left)
            r = dfs(node.right)
            nonlocal ans
            ans = max(ans, l + r + 2)
            return max(l, r) + 1
        dfs(root)
        return ans