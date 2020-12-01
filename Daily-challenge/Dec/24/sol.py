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