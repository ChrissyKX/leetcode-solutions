## Solution: Sort + Longest Increasing Subsequence

from bisect import bisect_left
from functools import cmp_to_key

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def cmp(e1, e2):
            if e1[0] == e2[0]:
                # if widths are equal, order heights in descending order so that envelopes 
                # with same widths and increasing heights do not count
                return e2[1] - e1[1]
            else:
                return e1[0] - e2[0]
        
        envelopes.sort(key=cmp_to_key(cmp))
        heights = []
        for e in envelopes:
            heights.append(e[1])
                    
        return self.LIS(heights)

    def LIS(self, nums):
        dp = []
        for n in nums:
            i = bisect_left(dp, n)
            if i == len(dp):
                dp.append(n)
            else:
                dp[i] = n
                
        return len(dp)
