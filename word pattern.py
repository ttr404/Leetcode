class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False 
        pattern_to_word_map = {}
        word_to_pattern_map = {}

        for ch, w in zip(pattern, words):
            if ch in pattern_to_word_map and pattern_to_word_map[ch] != w:
                return False
            if w in word_to_pattern_map and word_to_pattern_map[w] != ch:
                return False
            pattern_to_word_map[ch] = w
            word_to_pattern_map[w] = ch

        return True
        