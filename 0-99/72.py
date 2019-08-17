class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        len1 = len(word1)
        len2 = len(word2)

        dp = [[0 for _ in range(len1+1)] for _ in range(len2+1)]

        for i in range(len2+1):
            for j in range(len1+1):
                if j == 0:
                    dp[i][j] = i
                elif i == 0:
                    dp[i][j] = j
                else:
                    if word2[i-1] == word1[j-1]:
                        dp[i][j] = 1 + min(min(dp[i][j-1], dp[i-1][j]), dp[i-1][j-1] - 1)
                    else:
                        dp[i][j] = 1 + min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1])

        return dp[len2][len1]
