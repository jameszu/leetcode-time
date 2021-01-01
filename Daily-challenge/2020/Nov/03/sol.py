class Solution:
    def maxPower(self, s: str) -> int:
        i = 1
        n = len(s)
        count = 1
        res = 1
        while i < n:
            if s[i] == s[i-1]:
                count += 1
                res = max(res, count)
            else:
                # res = max(res, count)
                count = 1
            i += 1
        return res