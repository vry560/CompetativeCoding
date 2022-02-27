class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mem ={}
        mem[2] = ["a","b","c"]
        mem[3] = ["d","e","f"]
        mem[4] = ["g","h","i"]
        mem[5] = ["j","k","l"]
        mem[6] = ["m","n","o"]
        mem[7] = ["p","q","r","s"]        
        mem[8] = ["t","u","v"]
        mem[9] = ["w","x","y","z"]
        
        res = deque([""])
        for i in digits:
            for k in range(len(res)):
                a = res.popleft()
                for l in mem[int(i)]:
                    res.append(a+l)
        return res if len(res)>1 else []
