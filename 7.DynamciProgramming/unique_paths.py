# There is a robot on an m x n grid. The robot is initially located at 
# the top-left corner (i.e., grid[0][0]). The robot tries to move to 
# the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of 
# possible unique paths that the robot can take to reach the bottom-right corner.
# 61 leetcode

# dp[m-1][n-1] = dp[m-2][n-1] + dp[m-1][n-2]

def uniquePaths(self, n: int, m: int) -> int:
        dp = [[0 for i in range(m)] for j in range(n)] 
        for i in range(n):
            dp[i][0]= 1
        for i in range(m):
            dp[0][i]= 1
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        print(dp)
        return dp[-1][-1] 

# Given a m x n grid filled with non-negative numbers, find a path from 
# top left to bottom right, which minimizes the sum of all numbers along its path.
# 64 leetcode

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)] 
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for j in range(1, m):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]