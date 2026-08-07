class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] += 1
            if freq[idx] == 2:
                return ch