class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set(nums)
        if len(dups) == len(nums):
            return False
        return True
