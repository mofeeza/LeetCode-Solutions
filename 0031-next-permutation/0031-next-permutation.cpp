class Solution {
public:
    void nextPermutation(std::vector<int>& nums) {
        int n = nums.size();
        int i = n - 2;

        // Find the first element that is smaller than its right neighbor
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        if (i >= 0) {
            int j = n - 1;
            // Find the first element that is greater than nums[i]
            while (j > i && nums[j] <= nums[i]) {
                j--;
            }
            // Swap nums[i] and nums[j]
            std::swap(nums[i], nums[j]);
        }

        // Reverse the elements to the right of index i
        std::reverse(nums.begin() + i + 1, nums.end());
    }
};
