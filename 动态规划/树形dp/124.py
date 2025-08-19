from typing import List, Optional
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(node):
            if node is None:
                return 0
            
            l = max(dfs(node.left), 0)
            r = max(dfs(node.right), 0)
            nonlocal ans
            ans = max(ans, l + r + node.val)
            return max(l, r) + node.val
        dfs(root)
        return ans