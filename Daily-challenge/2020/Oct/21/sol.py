class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for item in asteroids:
            while stack and item < 0 < stack[-1]:
                if stack[-1] < -item:
                    stack.pop()
                    continue
                elif stack[-1] == -item:
                    stack.pop()
                break
                
            else:
                stack.append(item)
                
        return stack