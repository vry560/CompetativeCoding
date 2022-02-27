class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        p2, p1 = 0,nums[0]
        for i in range(1,n-1):
            t = max(p2+nums[i], p1)
            p2 = p1
            p1 = t
        mt = p1
        p2, p1 = 0,0
        for i in range(1,n):
            t = max(p2+nums[i], p1)
            p2 = p1
            p1 = t
        return max(mt, p1)
