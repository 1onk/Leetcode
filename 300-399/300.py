class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1 for _ in range(len(nums))]
        res = 1
        for i in range(1, len(nums)):
            tmp_max = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    tmp_max = max(tmp_max, dp[j] + 1)
            dp[i] = tmp_max
            print(dp)
            res = max(res, dp[i])
        return res