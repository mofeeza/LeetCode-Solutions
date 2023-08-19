class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Sum of natural numbers from 0 to n
        
        actual_sum = sum(nums)  # Sum of the elements in the array
        missing_number = expected_sum - actual_sum
        
        return missing_number
