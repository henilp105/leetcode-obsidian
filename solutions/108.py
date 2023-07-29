class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums==[]:
            return
        root=TreeNode(nums[len(nums)//2])
        root.left=self.sortedArrayToBST(nums[:len(nums)//2])
        root.right=self.sortedArrayToBST(nums[len(nums)//2+1:])
        return root