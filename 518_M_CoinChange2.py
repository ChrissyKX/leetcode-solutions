## My thoughts: We cannot use the coin change1 solution to approach this problem since there are multiple paths reaching amount i with the same combination (in different arrangement). In order for a path reaching dp[i] to be unique, we can ensure that the path is non-decreasing (fix an order). Since the path can end in any coin, at amount i, for each coin, we need to keep track of the number of non-decreasing paths ending in that coin. This makes the problem a 2D-DP problem. 

## In my initial algo, to compute amount i and coin j, I sum dp[i - c][0:j + 1]. However, tnis causes repeated calculation, since for amounti and coin j + 1, I sum dp[i - c][0:j + 2]. Hence, instead of the number of non-decreasing paths ending in coin[j], we store the cumulative number summing over coin[0:j + 1] at dp[i][j]. Then dp[i][j] = dp[i - c][j] + dp[i][j - 1]

## Leetcode Solution: The DP table is the same, except that the interpretation is smarter. The first dimension is still the amount, while the second dimension now is the available coin to use. dp[i][0] means 0 coins to use, dp[i][1] means the first coin, dp[i][2] means the first and the second coins, etc. The transition function is: dp[i][j] = dp[i - c][j] + dp[i][j - 1], meaning the number of combinations with only 0 to j - 1 coins plus the number of combinations in the left-out amount if we reserve a 5-coin. Note that since this column adds a 5-coin type to the available coins, that column only needs to take care of adding the 5-coins into the combinations and "reserve only the 5-coin" when transitioning.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        
        dp = [[1] * (len(coins) + 1) if i == 0 else [0] * (len(coins) + 1) \
              for i in range(amount + 1)]
        ans_col = 0
        
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                c = coins[j]
                if i < c:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - c][j] + dp[i][j - 1]
                
        return dp[amount][len(coins) - 1]
