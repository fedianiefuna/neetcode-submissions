class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak = 0
        max_streak = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                streak += 1
                max_streak = max(max_streak, streak)
            else:
                streak = 0
        return max_streak

        