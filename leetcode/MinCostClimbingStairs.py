class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        prev,cur = cost[0], cost[1]
        for i in range(2, len(cost)):
            t = cost[i]+min([cur, prev])
            prev = cur
            cur=t
        return min([cur, prev])
