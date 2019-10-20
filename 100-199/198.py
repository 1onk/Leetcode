class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = [0 for _ in range(length)]
        res = 0
        for i, v in enumerate(nums):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i], nums[0])
            else:
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            res = max(dp[i], res)
        return res