class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        sum-=root.val
        if not root.left and not root.right and sum==0: return True
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)