class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -10000 - 1
        max_ending_here = 0
        a = nums
        size = len(nums)
        for i in range(0, size):
            max_ending_here = max_ending_here + a[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
    
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far