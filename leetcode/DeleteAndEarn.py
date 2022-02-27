class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0]*(max(nums)+1)
        for i in nums:
            dp[i]+=i
        for i in range(2, len(dp)):
            dp[i] = max(dp[i]+dp[i-2], dp[i-1])
        return dp[-1]
