# Buddy Strings
Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
Example 2:

Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
Example 3:

Input: A = "aa", B = "aa"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Constraints:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist of lowercase letters.<br>

---
## Idea
Went to the wrong direction at the first rip. Bascially some if statements to determine if its buddies. <br>
if size of A is not same as size of B, then return False <br>
otherwise when A and B has any element that are not common, then return False <br>
otherwise when A is same as B and all characters are distinct in A, then return False <br>
otherwise, count:= 0 for i in range 0 to size of A, do if A[i] is not same as B[i], <br>
then count := count + 1 <br>
if count is same as 3, then return False <br>
return True

## Code
```python
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:

            
        lena = len(A)
        lenb = len(B)
        if lena != lenb:
            return False
        elif sorted(A) != sorted(B):
            return False
        elif A==B and len(set(A))==len(A):
            return False
        else:
            count = 0
            for i in range(lena):
                if A[i] != B[i]:
                    count += 1
                    if count == 3:
                        return False
            return True
```