# Basic Calculator II
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.<br>

## Idea
Just do while loop and convert to decimal

## Code
```python
class Solution:
    def calculate(self, s: str) -> int:
        op = '+'
        pre = 0; num = 0; res = 0
        for c in s+'+':
            if c.isdigit():
                num = 10*num + int(c)
            elif c in '+-*/':
                if op == '+': 
                    res += pre
                    pre = num
                elif op == '-': 
                    res += pre
                    pre = -num
                elif op == '*': 
                    pre = pre*num
                elif op == '/':
                    pre = int(pre/num)
                num = 0 
                op = c
        return res+pre
        
```