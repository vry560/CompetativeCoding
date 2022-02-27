class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0,1,1]
        for i in range(2,n):
            t=sum(arr)
            arr[0] = arr[1]
            arr[1] = arr[2]
            arr[2] = t
        return  arr[n] if n<3 else arr[-1]
