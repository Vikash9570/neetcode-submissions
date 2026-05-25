class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currcount=0
        result=0
        for num in nums:
            if num==1: 
                currcount+=1
            if num==0:   
                result =  max(currcount,result)
                currcount=0
                

        return max(currcount,result)