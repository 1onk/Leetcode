class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        num1, num2 = 0, 0
        for num in nums:
            xor ^= num
        mask = 1
        while xor & mask == 0:
            mask = mask << 1

        for num in nums:
            if num & mask == 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]


# https://blog.csdn.net/fuxuemingzhu/article/details/79434100#_30
# https://blog.csdn.net/qq_38595487/article/details/81163737