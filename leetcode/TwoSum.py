class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rmap={}
        tup = [(nums[i],i) for i in range(0,len(nums))]
        tup.sort()
        print(tup)
        i,j=0,len(tup)-1
        while(i<j):
            while(tup[i][0]+tup[j][0]>target):
                j-=1
            while(tup[i][0]+tup[j][0]<target):
                i+=1
            if(tup[i][0]+tup[j][0]==target):
                return [tup[i][1], tup[j][1]]
