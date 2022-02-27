class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        slider = [0]*len(grid[0])
        slider[0]=grid[0][0]
        for i in range(1, len(grid[0])):
            slider[i]=slider[i-1]+grid[0][i]
            
        for i in range(1, len(grid)):
            slider[0]=slider[0]+grid[i][0]
            for j in range(1, len(grid[i])):
                slider[j]=min((slider[j], slider[j-1]))+grid[i][j]
                
        return slider[-1]
