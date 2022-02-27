class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 2]
        for i in range(2, n):
            dp.append(dp[-1]+dp[-2])
        return dp[n]
