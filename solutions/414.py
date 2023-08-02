class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        t = list(set(nums))
        t.sort(reverse=True)
        try: return t[2]
        except: return t[0]