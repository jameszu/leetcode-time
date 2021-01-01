# Repeated DNA Sequences
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

0 <= s.length <= 105
s[i] is 'A', 'C', 'G', or 'T'.<br>

## Idea
Just do it. <br>
Actually just parse the string to hashtable and see what occured twice or more.

## Code
Simple
```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dict1 = {}
        lst = []
        for i in range(len(s)-9):
            if s[i:i+10] not in dict1:
                dict1[s[i:i+10]] = 1
            else:
                dict1[s[i:i+10]] += 1
        # print(dict1)
        for x in dict1:
            if dict1[x] != 1:
                lst += [x]
        return lst
```