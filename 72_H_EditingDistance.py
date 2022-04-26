## Solution: DP, 2d
## CAUTION: when bottom-up does not make sense to you, think the other way around using top-down

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        for i in range(len(word2) + 1):
            dp[i][0] = i
        for j in range(len(word1) + 1):
            dp[0][j] = j
        
        for i in range(len(word2)):
            for j in range(len(word1)):
                cur_dis = 0 if word2[i] == word1[j] else 1
                dp[i + 1][j + 1] = min([
                    dp[i][j] + cur_dis,
                    dp[i][j + 1] + 1,
                    dp[i + 1][j] + 1
                ])
                
        return dp[len(word2)][len(word1)]
                
        
