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
            c1 = (lo + hi) // 2
            c2 = m + n - c1
            Lmax1 = float('-inf') if c1 == 0 else nums1[(c1-1) // 2]
            Rmin1 = float('inf') if c1 == 2 * n else nums1[c1 // 2]
            Lmax2 = float('-inf') if c2 == 0 else nums2[(c2-1) // 2]
            Rmin2 = float('inf') if c2 == 2 * m else nums2[c2 // 2]

            if Lmax1 > Rmin2:
                hi = c1 - 1
            elif Lmax2 > Rmin1:
                lo = c1 + 1
            else:
                break

        return (max(Lmax1, Lmax2) + min(Rmin1, Rmin2)) / 2
