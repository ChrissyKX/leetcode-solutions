class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         # Method 1: DP
#         # O(N), O(1)
#         none_prof = 0
#         hold_prof = -10001
        
#         for i in range(len(prices)):
#             none_prof = max(hold_prof + prices[i], none_prof)
#             hold_prof = max(-prices[i], hold_prof)
            
#         return none_prof

        # Method 2: Sliding window
        # O(N), O(1)
        buy, sell = sys.maxsize, sys.maxsize
        result = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                result = max(result, sell - buy)
                buy = prices[i]
                sell = buy
            elif prices[i] > sell:
                sell = prices[i]
         
        result = max(result, sell - buy)
        return result
