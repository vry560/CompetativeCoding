class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque([nums[0]])
        for i in range(1,k):
            while dq and nums[i] > dq[-1]:
                dq.pop()
            dq.append(nums[i])
        res=[dq[0]]     
        for end in range(k,len(nums)):
            if nums[end-k] == dq[0]:
                dq.popleft()
            while dq and nums[end] > dq[-1]:
                dq.pop()
            dq.append(nums[end])
            res.append(dq[0])  
        return res
