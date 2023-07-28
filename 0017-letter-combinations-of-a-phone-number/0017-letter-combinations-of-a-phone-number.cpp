class Solution {
public:
    std::vector<std::string> letterCombinations(std::string digits) {
        std::vector<std::string> result;
        if (digits.empty()) return result;

        std::vector<std::string> mapping = {
            "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        };

        std::string currentCombination;
        generateCombinations(digits, 0, mapping, currentCombination, result);
        return result;
    }

private:
    void generateCombinations(const std::string& digits, int index, const std::vector<std::string>& mapping,
                              std::string& currentCombination, std::vector<std::string>& result) {
        if (index == digits.length()) {
            result.push_back(currentCombination);
            return;
        }

        int digit = digits[index] - '0';
        for (char ch : mapping[digit]) {
            currentCombination.push_back(ch);
            generateCombinations(digits, index + 1, mapping, currentCombination, result);
            currentCombination.pop_back();
        }
    }
};
