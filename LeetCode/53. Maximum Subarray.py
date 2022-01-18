class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentNums=nums[0];
        overallNums=nums[0];
        for i in range(len(nums)):
            
            if(currentNums>0):
                currentNums+=nums[i];
            else:
                currentNums=nums[i];

            if(currentNums>overallNums):
                overallNums=currentNums;

        return overallNums;            


