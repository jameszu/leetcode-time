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