class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False 
        p2w = {}
        w2p = {}

        for ch, w in zip(pattern, words):
            if ch in p2w and p2w[ch] != w:
                return False
            if w in w2p and w2p[w] != ch:
                return False
            p2w[ch] = w
            w2p[w] = ch

        return True
        