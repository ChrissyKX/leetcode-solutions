# Solution: DP, position i as the last number of the subarray
# CAUTION: I thought using prefix sums could work (max prefix sum - min prefix sum gives the answer).
#          However, the max prefix sum is not necessarily to the right of the min prefix sum, so it gives wr#          wrong answers. 
# Reflection: 
#          1. Before submitting, think about edge cases (all kinds of input).
#          2. Before using a previously established method, carefully examine whether they would work 
#             for all cases.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
                
        return max(nums)
