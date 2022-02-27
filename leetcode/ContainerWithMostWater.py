class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
	i,j = 0, len(height)-1
        m = 0
        while i<j :
            while j>-1 and height[i] >= height[j]:
                m = max([m,  height[j]*(j-i)])
                j-=1
            while i<len(height) and height[i] < height[j]:
                m = max([m,  height[i]*(j-i)])
                i+=1
        return m
