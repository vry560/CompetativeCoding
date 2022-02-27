class Solution(object):
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        mem = {}
        mem[1]=set(["()"])
        
        for i in range(2,n+1):
            res=set()
            s1 = mem[i-1]
            for val in s1:
                for j in range(len(val)):
                    res.add(val[:j]+"()"+val[j:])
            mem[i]=res
        return mem[n]
