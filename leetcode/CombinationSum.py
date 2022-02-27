class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        val = [[] for i in range(target+1)]
	for c in candidates:
            for i in range(1,target+1):
                if i>c:
                    for k in val[i-c]:
                        val[i].append(k+[c])
                elif i==c:
                    val[i].append([c])
            
        return val[target]
