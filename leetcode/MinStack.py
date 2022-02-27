class MinStack(object):
    

    def __init__(self):
        self.stack = []
        self.m = [float('inf')]
        
    
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if(self.m[-1] >= val):
            self.m.append(val)
        self.stack.append(val)
        
        

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if(val == self.m[-1]):
            self.m.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.m[-1]
