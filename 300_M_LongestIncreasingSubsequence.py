## Solution: DP, dp[i] as the end of the list

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        result = 1

        for i in range(len(nums)):
            for j in range(i):
                if (nums[j] < nums[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])

        return result
