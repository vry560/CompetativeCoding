class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        mi=n
        dp=[i for i in range(n+1)]
        dp[1]=1
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = min([dp[i], max([j, dp[i-j]+1])])
        return dp[n]
