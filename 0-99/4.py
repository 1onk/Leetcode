# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/4-xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-shu/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        Lmax1, Lmax2, Rmin1, Rmin2, c1, c2 = 0, 0, 0, 0, 0, 0
        lo, hi = 0, 2 * n

        while lo <= hi:
