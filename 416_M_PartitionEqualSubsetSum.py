## Solution: DP, 2D problem with 1D optimization

## CAUTION: When optimizing space complexity using 1D array, think about the transition function to see whether dp[i] relies on values from the previous level or the current. If from previous level, we need to iterate reversely.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = int(target / 2)
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        for i in range(len(nums)):
            num = nums[i]
            for j in range(target, num - 1, -1):   
                if i == 0 and j == num:
                    dp[j] = True
                    continue

                dp[j] = dp[j] or dp[j - num]
                    
                if j == target and dp[j]:
                    return True

        return dp[-1]
                
        
