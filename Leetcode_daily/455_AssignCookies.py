class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i = 0
        j = 0
        co = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                co += 1
                i += 1
                j += 1
            else:
                j += 1

        return co