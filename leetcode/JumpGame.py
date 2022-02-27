class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mx = 0
        l=len(nums)
        for i in range(len(nums)):
            mx = max(mx, i+nums[i])
            if mx == i and i != l-1:
                return False
        return mx >= l-1
