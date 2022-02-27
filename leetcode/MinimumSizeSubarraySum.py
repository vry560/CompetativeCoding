class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        i,j=0,0
        mi = float('inf')
        s=0
        for j in range(len(nums)):
            s+=nums[j]
            while i<=j and s>=target:
                s-=nums[i]
                i+=1
                mi = min([mi, j-i+2])
        return 0 if mi > len(nums) else mi
