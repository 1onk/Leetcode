class NumArray:

    def __init__(self, nums: List[int]):
        sums = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            sums[i + 1] = sums[i] + nums[i]
        self.sums = sums

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)