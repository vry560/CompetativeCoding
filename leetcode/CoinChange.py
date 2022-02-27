class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        arr=[-1]*(amount+1)
        arr[0]=0
        for i in coins:
            if i<=amount:
                arr[i]=1
        for i in range(amount+1):
            if arr[i] == -1:
                m = []
                for j in coins:
                    if j<i and arr[i-j]!=-1:
                        m.append(arr[i-j]+1)
                if len(m)>0:
                    arr[i]=min(m)
        return arr[amount]
