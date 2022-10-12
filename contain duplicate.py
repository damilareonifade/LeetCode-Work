class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        y = set(nums)
        if len(y) < len(nums):
            return True
        else:
            return False
