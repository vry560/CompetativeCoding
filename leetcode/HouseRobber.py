class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, nums[0]]
        for i in range(1,len(nums)):
            dp.append(max([dp[-1], dp[-2]+nums[i]]))
        return dp[-1]
