class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c=0
        temp=l1.val+l2.val+c
        c=int(temp/10)
        res = ListNode(temp%10, None)
        l1=l1.next
        l2=l2.next
        ans=res
        
        while l1 != None or l2 != None or c!=0:
            tl2 = 0 if(l2 == None) else l2.val
            l2= l2 if(l2 == None) else l2.next
            tl1 = 0 if(l1 == None) else l1.val
            l1 = l1 if(l1 == None) else l1.next 
            temp=tl1+tl2+c
            c=int(temp/10)
            tres = ListNode(temp%10, None) 
            res.next=tres
            res=res.next
        return ans
