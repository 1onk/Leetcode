"""
1122.数组的相对排序
地址：https://leetcode-cn.com/problems/relative-sort-array/

利用Counter记录个数，在遍历
"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        d = Counter(arr1)
        res = []
        for i in arr2:
            for k in range(d[i]):
                res.append(i)
        temp = []
        for i in arr1:
            if i not in arr2:
                temp.append(i)
        temp.sort()
        
        return res + temp