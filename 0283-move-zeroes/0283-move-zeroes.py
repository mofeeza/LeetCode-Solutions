class Solution(object):
    def moveZeroes(self, nums):

        non_zero_index = 0  # Initialize the pointer for the position of the next non-zero element

        # Loop through the array and move non-zero elements to their correct positions
        for i in range(len(nums)):
            if nums[i] != 0:
                # If the current element is non-zero, move it to the position indicated by non_zero_idx
                nums[non_zero_index] = nums[i]
                non_zero_index += 1

        # Fill the rest of the array with zeros after all non-zero elements are moved
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0