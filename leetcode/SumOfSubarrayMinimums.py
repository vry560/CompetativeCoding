class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        md = 10**9 + 7
        stack = [0]
        arr = [0]+arr+[0]
        res=0
        for i in range(1,len(arr)):
            stindx = i
            while stack and arr[stack[-1]] > arr[i]:
                cur = stack.pop();
                res += arr[cur]*(cur-stack[-1])*(i-cur)
            stack.append(i)
        return res % md
