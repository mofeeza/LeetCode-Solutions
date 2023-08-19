class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningsum = []
        runningsum.append(nums[0])
        
        for i in range(1 , len(nums)):
            runningsum.append(nums[i] + nums[i-1])
            nums[i] += nums[i-1]
        return runningsum