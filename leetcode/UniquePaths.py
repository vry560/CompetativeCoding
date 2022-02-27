class Solution(object):
    def uniquePaths(self, m, n):
        arr=[1]*m
        for i in range(1, n):
            tmp = [1]+[0]*(m-1)
            for j in range(1,m):
                tmp[j]=tmp[j-1]+arr[j]
            arr = tmp
        return arr[-1]
