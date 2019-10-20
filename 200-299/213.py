# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         length = len(nums)
#         dp = [0 for _ in range(length)]
#         flag = [False for _ in range(length)]
#         res = 0
#         for i, v in enumerate(nums):
#             if i == 0:
#                 dp[i] = nums[i]
#                 flag[i] = True
#             elif i == 1:
#                 if nums[i] >= nums[0]:
#                     dp[i] = nums[i]
#                     flag[i] = False
#                 else:
#                     dp[i] = nums[0]
#                     flag[i] = True
#             elif i == length - 1:
#                 if dp[i-2]+nums[i] > dp[i-1]:
#                     dp[i] = nums[i] + dp[i-2]
#                     if flag[i-2] == True:
#                         dp[i] -= nums[0]
#                 elif dp[i-2]+nums[i] == dp[i-1] and flag[i-2] == False:
#                     dp[i] = nums[i] + dp[i-2]
#                 else:
#                     dp[i] = dp[i-1]
#                     if flag[i-1] == True:
#                         dp[i] -= nums[0]
#             else:
#                 if nums[i]+dp[i-2] > dp[i-1]:
#                     dp[i] = nums[i]+dp[i-2]
#                     flag[i] = flag[i-2]
#                 elif nums[i]+dp[i-2] == dp[i-1] and flag[i-2] == False:
#                     dp[i] = nums[i]+dp[i-2]
#                 else:
#                     dp[i] = dp[i-1]
#                     flag[i] = flag[i-1]
#             res = max(dp[i], res)
#             print(dp)
#             print(flag)
#         return res
#
# [2,2,4,3,2,5]



class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        dp = [0 for _ in range(length)]
        res = 0
        for i in range(length-1):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i], dp[i-1])
            else:
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            res = max(dp[i], res)
        for i in range(1, length):
            if i == 1:
                dp[i] = nums[i]
            elif i == 2:
                dp[i] = max(nums[i], dp[i-1])
            else:
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            res = max(dp[i], res)
        return res