## Some thoughts on DP: 
## 1. Think about possible components of a solution. For example, in editing distance, every pair of characters can be matched, and thus the dp array is fully filled. However, in LCS, only two identical characters can be paired. We don't need to consider the other pairs nor to fill the dp array completely. This is usually also the "choices" part of the DP approach.
## 2. DP solution can be retroactive or predictive. 
##  - Retroactive: dp[i][j] = solve(i - 1, j - 1) + 1 We want to know the solution to the
##    subproblem(i, j), so we contrust it from previous subproblems. 
##  - Predictive: dp[i +1][j + 1] = dp[i][j] + 1 We already know the solution to the 
##    subproblem(i, j), and the choices are clear, so for a certain choice that leads to
##    subproblem(i + 1, j + 1), we can compute an answer for that subproblem (not necessarily 
##    the optimal solution, since other subproblems + some choice may also lead to subproblem
##    (i + 1, j + 1)).

## About this problem:
## The key of this problem is the following:
## 1. If we connect matching characters in the two strings with lines, LCS should not contain any crossing lines. 
## 2. This comes from the greedy approach: Always pick the the leftmost possible (does not overlap with the current LCS) matching character. This is because picking the leftmost match gives the highest possibility for the rest of the two texts to match. It can be easily generalized if the texts are processed from right to left. This indicates that if we know the solution to LCS(text1[i + 1:], text2[j + 1:]) and text1[i] == text2[j], then the text1[i] and text[j] pair must be part of the solution.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * n for _ in range(m)]
        
        def getDP(i, j):
            nonlocal m, n
            if i >= m or j >= n:
                return 0
            return dp[i][j]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = getDP(i + 1, j + 1) + 1
                else:
                    # only one of text1[i] and text2[j] can be part of the solution,
                    # since no crossing lines allowed
                    dp[i][j] = max(getDP(i + 1, j), getDP(i, j + 1))
                
        return dp[0][0]

     def longestCommonSubsequenceV2(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            prev_diag = dp[-1]
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    tmp = dp[j]
                    dp[j] = prev_diag + 1
                    prev_diag = tmp
                else:
                    # only one of text1[i] and text2[j] can be part of the solution,
                    # since no crossing lines allowed
                    tmp = dp[j]
                    dp[j] = max(dp[j], dp[j + 1])
                    prev_diag = tmp

        return dp[0]
