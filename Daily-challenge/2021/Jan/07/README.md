# Longest Substring Without Repeating Characters

Solution
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.<br>

## Idea

## Code
```python
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
        
```