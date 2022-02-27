class Solution(object):
    
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        tmp=[0 for i in range(k+1)]
        m=0
        while(tmp[k] < n):
            t=k
            m+=1
            for j in range(t,0,-1):
                tmp[j]+=tmp[j-1]+1
        return m
