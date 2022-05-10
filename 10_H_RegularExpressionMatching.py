## Complexity: Space: O(M*N), Time: O(M*N)

## Key points:
## 1. Base cases are not just solely True/False. When the length of the text is 0, the text can match a series of '*' elements. Hence, if the dp[i][j] stores the subproblem isMatch(s[j:], p[i:]), dp[i][len(s)] should be True as long as p[i] is a '*' element, startimg from i=len(p) until we reaches a p[i] that is not a '*' element.

## 2. In my initial version, when encoutering '*' element, I traced text2 all the way down to the point where it does not match the '*' element and check each subproblem on the way. However, this is an deviation from the DP思想, since we'll perform the tracing down again at the next levels. The right thing to do is to think about only the current level (i and j). For the current level, we either match with the '*' element or not. 

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(p)
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True
        
        for i in range(m - 1, -1, -1):
            for j in range(n, -1, -1):
                match = j < n and (p[i] == '.' or p[i] == s[j])
                if i + 1 < m and p[i + 1] == '*':
                    # 1. not matching '*' pattern with the input string
                    # 2. matching ...
                    dp[i][j] = dp[i + 2][j] or (match and dp[i][j + 1])
                else:
                    dp[i][j] = match and dp[i + 1][j + 1]
                    
        return dp[0][0]
                    
        
        
        
            
                
                        
                        
        
