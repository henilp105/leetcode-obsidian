class Solution:
    def maxDepth(self, root: TreeNode, d = 0) -> int:
        return max(self.maxDepth(root.left, d + 1), self.maxDepth(root.right, d + 1)) if root else d