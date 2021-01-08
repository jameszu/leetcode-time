class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        used = {}
        for idx in range(len(s)):
            if s[idx] in used and i <= used[s[idx]]:
                i = used[s[idx]] + 1
                
            else:
                j = max(j, idx - i + 1)
                
            used[s[idx]] = idx
            
        return j