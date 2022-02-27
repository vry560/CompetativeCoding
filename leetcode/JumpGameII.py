class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        mx,jp,i=0,0,0
        while (i<l and mx < l-1):
            jp+=1
            j,t=i,mx
            while(j<l and j<=mx):
                t=max([t,j+nums[j]])
                j+=1
            i,mx=j-1,t
        return jp
