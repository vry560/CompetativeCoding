class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        vol=0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                k = stack.pop()
                if stack:
                    mi = min([height[stack[-1]], height[i]])
                    vol += (mi - height[k])*(i-stack[-1]-1)
            stack.append(i)
        return vol
