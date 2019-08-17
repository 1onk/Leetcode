class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                tmp = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    tmp += 1
                res = max(res, tmp)
        return res