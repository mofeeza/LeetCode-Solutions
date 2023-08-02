class Solution(object):
    def lengthOfLastWord(self, s):
        
        # Initialize a variable to keep track of the length of the last word
        last_word_length = 0

        # Start iterating from the end of the string
        i = len(s) - 1

        # Skip any trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count the characters of the last word
        while i >= 0 and s[i] != ' ':
            last_word_length += 1
            i -= 1

        return last_word_length
