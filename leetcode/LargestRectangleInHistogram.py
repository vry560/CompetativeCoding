class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        heights.append(0)
        m = 0
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                k = stack.pop()
                m = max([m, heights[k]*(i-stack[-1]-1)])
            stack.append(i)
        return m
