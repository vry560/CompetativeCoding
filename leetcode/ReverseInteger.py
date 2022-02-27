class Solution:
    def reverse(self, x: int) -> int:
        li= 1<<31;
        if x<0:
            k = -1
            abs_x = -1*x
        else:
            k = 1
            abs_x = x
        rev = 0
        while(abs_x>0):
            rev=rev*10+(abs_x%10)
            abs_x=abs_x//10
        res = rev*k
        if (res>li-1 or res<li*-1):
            return 0
        return res
