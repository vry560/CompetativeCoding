class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur = 1
        prev = 0
        for i in range(1, n):
            t = cur+prev
            prev=cur
            cur=t
        return prev if n == 0 else cur
