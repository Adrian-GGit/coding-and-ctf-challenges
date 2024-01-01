class Solution(object):
    def modify_char_counter(self, letters, char, modify_by):
        if char not in letters:
            letters[char] = 0
        letters[char] = letters[char] + modify_by


    def canConstruct(self, ransomNote, magazine):
        if len(magazine) < len(ransomNote):
            return False

        letters = {}
        for i, char in enumerate(magazine):
            self.modify_char_counter(letters, char, 1)
            if i < len(ransomNote):
                self.modify_char_counter(letters,  ransomNote[i], -1)

        return all([counter >= 0 for counter in letters.values()])