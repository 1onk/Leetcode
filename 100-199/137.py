class Solution:
    def singleNumber(self, nums: [int]) -> int:
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num # ones & num 提取两个数都为1的位，与twos作或操作保留出现2次的位
            ones ^= num  # 当 ones 和 num 同时为 1 or 0 时，ones = 0，因为同时为1已经加到twos里了，这里不做count
            threes = ones & twos # 当ones和twos对应位都为1时，说明此位出现了3次
            ones &= ~threes # three为1的位，将one和two对应位归零
            twos &= ~threes
        return ones

# 如果能设计一个状态转换电路，使得一个数出现3次时能自动抵消为0，最后剩下的就是只出现1次的数。使用两个bit a和b分别来记录该位上实际的值~
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for num in nums:
            b = b ^ num & ~a
            a = a ^ num & ~b
        return a|b