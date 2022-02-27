class Solution:
    def binser(self,n,t):
        i,j=0,len(n)
        while(i!=j):
            k=int((i+j)/2)
            if(n[k]>=t):
                j=k
            elif(n[k]<t):
                i=k+1
        return i-1
        
        
    def ksel(self,n1,n2,t): 
        m,n=len(n1)-1,len(n2)-1
        if(m==-1):
            return n2[t]
        elif(n==-1):
            return n1[t]
        if(t>m):
            n2id=t-m-1
            k=n2[n2id]
            indx=self.binser(n1,k)
            if(indx==m):
                return k
            return self.ksel(n1[indx+1:],n2[n2id+1:],t-indx-n2id-2)
        else:
            k=n1[t]
            indx=self.binser(n2,k)
            if(indx==-1):
                return k
            return self.ksel(n1[:t],n2[:indx+1],t)
            
            
    
    
    
    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:
        m,n=len(n1)-1,len(n2)-1
        tl=(m+n)
        if(tl%2==0):
            t=int(tl/2)
            k=[t,t+1]
        else:
            k=[int((tl-1)/2)+1]
        m=0.0
        for t in k:
            m += self.ksel(n1,n2,t)
        return m/len(k)
