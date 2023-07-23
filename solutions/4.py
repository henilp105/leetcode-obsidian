class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)
        
        # If the combined array has an odd number of elements, return the middle element
        if n % 2 == 1:
            return nums[n // 2]
        # Otherwise, return the average of the two middle elements
        else:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2