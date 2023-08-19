class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_counts = {}
        magazine_counts = {}
        
        # Count character frequencies in ransomNote and magazine
        for i in ransomNote:
            ransom_counts[i] = ransom_counts.get(i, 0) + 1
        
        for i in magazine:
            magazine_counts[i] = magazine_counts.get(i, 0) + 1
        
        # Check if characters in ransomNote can be constructed from magazine
        for i, count in ransom_counts.items():
            if i not in magazine_counts or magazine_counts[i] < count:
                return False
        
        return True
