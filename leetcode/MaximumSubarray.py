class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        mi = s
        mx = nums[0]
        for i in range(len(nums)):
            t=s+nums[i]
            mx = mx if mx > t-mi else t-mi
            mi = mi if mi<t else t
            s=t
        return mx
