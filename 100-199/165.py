class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = ([*map(int, v.split('.'))] for v in (version1, version2))
        d = len(v2) - len(v1)
        v1, v2 = v1 + [0] * d, v2 + [0] * -d
        return (v1 > v2) - (v1 < v2)

version1 = "7.5.2.4"
version2 = "7.5.3"
print(Solution().compareVersion(version1, version2))