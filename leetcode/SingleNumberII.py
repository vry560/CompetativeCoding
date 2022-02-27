class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=[0]*32
        res = 0
        for i in nums:
            t = i
            j=0
            while t != 0 and j < 32:
                k[j] += t & 1
                t >>= 1
                j += 1
        for i in k[::-1]:
            res = (res << 1) + i%3
        
        return res if k[31]%3 == 0 else res - (1<<32)
