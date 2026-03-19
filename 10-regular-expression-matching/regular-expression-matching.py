class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)

        # DP table
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True   # empty matches empty

        # patterns like a*, a*b*, etc.
        for j in range(2, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, m+1):
            for j in range(1, n+1):

                # normal match or '.'
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]

                # star handling
                elif p[j-1] == '*':
                    # zero occurrence
                    dp[i][j] = dp[i][j-2]

                    # one or more occurrence
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]

        return dp[m][n]