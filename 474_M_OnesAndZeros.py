## Solution: 3D-dp with space optimization

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        for i in range(len(strs)):
            count0 = 0
            for c in strs[i]:
                if c == '0':
                    count0 += 1
            strs[i] = (count0, len(strs[i]) - count0)

        # Method2
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for k in range(len(strs)):
            count0 = strs[k][0]
            count1 = strs[k][1]
            for i in range(m, count0 - 1, -1):
                for j in range(n, count1 - 1, -1):
                    dp[i][j] = max(dp[i - count0][j - count1] + 1, dp[i][j])

        return dp[-1][-1]

#         # Method1
#         memo = {}

#         def recurse(strs, m, n, i, memo):
#             if i == len(strs) or (m == 0 and n == 0):
#                 return 0

#             if (m, n, i) not in memo:
#                 if m - strs[i][0] < 0 or n - strs[i][1] < 0:
#                     memo[(m, n, i)] = recurse(strs, m, n, i + 1, memo)
#                 else:
#                     memo[(m, n, i)] = max(recurse(strs, m - strs[i][0], n - strs[i][1], i + 1, memo) + 1,
#                                      recurse(strs, m, n, i + 1, memo))
#             return memo[(m, n, i)]

#         return recurse(strs, m, n, 0, memo)

