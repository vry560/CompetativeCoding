class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res={}
        r1=TreeNode()
        res[0]=[]
        res[1]=[r1]
        res[2]=[]
        for i in range(2,n,2):
            tmp=[]
            for j in range(1,i+1,2):
                l=res[j]
                r=res[i-j]
                if(len(l)!=0 and len(r)!=0):
                    for o in l:
                        for p in r:
                            rt=TreeNode()
                            rt.right=p
                            rt.left=o
                            tmp.append(rt)
            
            res[i+1]=tmp
        if(n in res):
            return res[n]
        else:
            return []
