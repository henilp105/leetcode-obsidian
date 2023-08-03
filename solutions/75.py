class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r,g,b = nums.count(0),nums.count(1),nums.count(2)
        for i in range(r):
            nums[i]=0
        for i in range(r,r+g):
            nums[i]=1
        for i in range(r+g,len(nums)):
            nums[i]=2