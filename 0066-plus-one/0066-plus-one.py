class Solution(object):
    def plusOne(self, digits):
        
        n = len(digits)
        carry = 1

        for i in range(n - 1, -1, -1):
            current_sum = digits[i] + carry
            digits[i] = current_sum % 10
            carry = current_sum // 10

        if carry:
            digits.insert(0, carry)

        return digits