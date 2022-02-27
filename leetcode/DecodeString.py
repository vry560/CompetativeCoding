class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in s:
            if(i != ']'):
                stack.append(i)
            else:
                tmp=""
                while(stack[-1]!="["):
                    tmp = stack.pop()+tmp 
                stack.pop()
                snum = ""
                while(len(stack)>0 and stack[-1].isdigit()):
                    snum = stack.pop() + snum
                num = int(snum)
                for i in range(num):
                    stack.append(tmp)
	return "".join(i for i in stack)
