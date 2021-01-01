# Remove duplicated letters
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.<br>

---
## Idea
interesting stack problem<br>
We need a hashmap that have the letter as the key and the index number as the value. <br>
Then we loop through the letters in the string, check if its in the stack, if so just skip. Otherwise check the value of the letter and the index of the letter using stack. <br>
So two conditions for updating the stack: 1 being the current letter has to be smaller than the last letter in the stack. 2 being the current index smaller than the last letter index value in the hashmap we created. <br>
For condition 1, it means there will be a letter that is smaller than the last letter in the stack. Combine with condition 2 we get the last letter in the stack is useless coz the current letter is smaller as well as int he hashmap theres a bigger index waiting. Hence we can just pop out the last letter. THen we just append the current letter to the stack<br>

## Code
```python
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        dict1 = {c: i for i, c in enumerate(s)}
        
        stack = []
        
        for i, c in enumerate(s):
            if c in stack: continue
            while stack:
                # Check the order first then check if its later than i
                if stack[-1] > c and i < dict1[stack[-1]]:
                    stack.pop()
                else:
                    break
                    
            stack.append(c)
            
            
        return ''.join(stack)
```