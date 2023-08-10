class Solution(object):
    def reverse(self, x):
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if (x >= 0):
            sign = 1
        else:
            sign = -1
        
        y = 0
        x = abs(x)
        
        while x > 0:
            lower = x % 10
            
            if (y > (INT_MAX - lower) / 10):
                return 0
            
            y = (y * 10) + lower
            x = x / 10
        
        return sign * y