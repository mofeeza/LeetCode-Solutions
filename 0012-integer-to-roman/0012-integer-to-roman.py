class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Define the mapping of Roman numerals and their corresponding values
        roman_numerals = [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1)
        ]
        
        roman_string = ''
        
        # Iterate through the Roman numerals and append the corresponding symbols
        for symbol, value in roman_numerals:
            while num >= value:
                roman_string += symbol
                num -= value
        
        return roman_string