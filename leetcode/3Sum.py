class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=set()
        if(len(nums)<3):
            return res
        rev_map={}
        for i in range(len(nums)):
            if nums[i] not in rev_map:
                rev_map[nums[i]] = set()
            rev_map[nums[i]].add(i)
        knums= rev_map.keys()
        
        if 0 in rev_map and len(rev_map[0])>=3:
            res.add((0,0,0))
            
        for i in range(len(knums)):
            if len(rev_map[knums[i]]) == 1 or knums[i] == 0:
                p=i+1
            else:
                p=i
            for j in range(p, len(knums)):
                k=-1*(knums[i]+knums[j])
                tmp = (knums[i],knums[j])
                if(k in tmp and len(rev_map[k])==1):
                    continue
                elif(k in rev_map):
                    tmp1= tuple(sorted((knums[i], knums[j], k)))
                    res.add(tmp1)
        return res
