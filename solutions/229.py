class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = list()
        k = list(set(nums))
        for i in k:
            if nums.count(i) > len(nums)//3:
                t.append(i)
        return list(set(t)) 