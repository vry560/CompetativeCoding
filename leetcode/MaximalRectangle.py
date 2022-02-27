class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        t=[0 for i in range(len(matrix[0])+2)]
        mxt=0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):          
                if matrix[i][j] == "0" :
                    t[j+1] = 0 
                else:
                    t[j+1]+=1
                    
            stack = []
            for i in range(len(t)):
                while stack and t[stack[-1]]>t[i]:
                    k = stack.pop()
                    mxt = max([mxt, t[k]*(i-stack[-1]-1)])
                stack.append(i)
        return mxt
