class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curnum = 0
        curstring = ''
        
        for c in s:
            if c == '[':
                stack.append(curstring)
                stack.append(curnum)
                curstring = ''
                curnum = 0
                
            elif c == ']':
                num = stack.pop()
                prevstring = stack.pop()
                curstring = prevstring + num* curstring
            elif c.isdigit():
                curnum = curnum * 10 + int(c)
            else:
                curstring += c
                
        return curstring