class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chset = {}
        p1,p2 = 0,0
        l = len(s)
        mx=0
        while p2<l and p1<=p2:
            k=s[p2]
            if k in chset:
                p1=p1 if p1 > chset[k]+1 else chset[k]+1
            chset[k] = p2  
            p2+=1
            curlen=p2-p1
            mx=mx if mx > curlen else curlen
        return mx
