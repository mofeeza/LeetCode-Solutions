class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:  # Check if the input list is empty
            return 0

        # Initialize the pointer for the position of the next unique element
        unique_index = 1

        # Loop through the array and move unique elements to their correct positions
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                # If the current element is different from the previous one, move it to the position indicated by unique_index
                nums[unique_index] = nums[i]
                unique_index += 1

        return unique_index