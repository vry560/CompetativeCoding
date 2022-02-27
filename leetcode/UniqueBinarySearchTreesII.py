class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def add(n, tree):
            if(tree != None):
                return TreeNode(tree.val+n, add(n, tree.left), add(n, tree.right))
            return None
        dp = [[] for i in range(n+1)]
        dp[0] = [None]
        dp[1] = [TreeNode(1)]
        for i in range(2,n+1):
            for j in range(i):
                for r in dp[j]:
                    for l in dp[i-j-1]:
                        dp[i].append(TreeNode(j+1, r, add(j+1,l)))
        # print dp
        return dp[n]
