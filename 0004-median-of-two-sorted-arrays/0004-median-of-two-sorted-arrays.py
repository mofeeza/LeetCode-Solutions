class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)

        lowervalue = len(merged) % 2
        uppervalue = len(merged) / 2

        if (lowervalue != 0):
            return merged[uppervalue]
        
        else:
            median = (merged[uppervalue] + merged[uppervalue - 1]) / 2.0
            return median