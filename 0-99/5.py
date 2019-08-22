# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if s == '':
#             return ''
#         l = len(s)
#         max_length = 0
#         palindromic = ''
#         for i in range(l):
#             x = 1
#             while (i - x) >= 0 and (i + x) < l:
#                 if s[i + x] == s[i - x]:
#                     x += 1
#                 else:
#                     break
#             x -= 1
#             if 2 * x + 1 > max_length:
#                 max_length = 2 * x + 1
#                 palindromic = s[i - x:i+ x + 1]
#
#             x = 0
#             if i + 1 < l:
#                 while (i - x) >= 0 and (i + 1 + x) < l:
#                     if s[i + 1 + x] == s[i - x]:
#                         x += 1
#                     else:
#                         break
#             x -= 1
#             if 2 * x + 2 > max_length:
#                 max_length = 2 * x + 2
#                 palindromic = s[i - x:i + x + 2]
#         if palindromic == '':
#             palindromic = s[0]
#         return palindromic


# class Solution:
#     # def longestPalindrome(self, s: str) -> str:
#     def longestPalindrome(self, s):
#         length = len(s)
#         max_length = 0
#         dp = [[False for _ in range(length)] for _ in range(length)]
#         res = ''
#         for i in range(length):
#             for j in range(length - i):
#                 if i == 0:
#                     res = s[0]
#                     dp[j][j] = True
#                 elif i == 1:
#                     if s[j] == s[j+1]:
#                         res = s[j:j+2]
#                         dp[j][j+1] = True
#                 else:
#                     print(j, j+i)
#                     if s[j] == s[j+i]:
#                         dp[j][j+i] = dp[j+1][j+i-1]
#                         if dp[j][j+i] and i > max_length:
#                             max_length = i
#                             res = s[j:j+i+1]
#         print(dp)
#         return res
# print(Solution().longestPalindrome("abcda"))

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        ss = '\0\1' + '\1'.join([x for x in s]) + '\1\2'
        p = [0] * len(ss)

        center = 0
        mx = 0
        max_str = ''
        for i in range(1, len(p) - 1):

            if i < mx:
                j = 2 * center - i
                p[i] = min(mx - i, p[j])

            while ss[i - p[i] - 1] == ss[i + p[i] + 1]:
                p[i] += 1

            if i + p[i] > mx:
                mx = i + p[i]
                center = i

            if 1 + 2 * p[i] > len(max_str):
                max_str = ss[i - p[i]:i + p[i] + 1]

        return max_str.replace('\1', '')