# Valid Square

Solution
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
 

Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.<br>

## Idea

## Code
```python
class Solution:
    def validSquare(self, p1, p2, p3, p4):
        if p1==p2==p3==p4:return False
        def dist(x,y):
            return (x[0]-y[0])**2+(x[1]-y[1])**2
        ls=[dist(p1,p2),dist(p1,p3),dist(p1,p4),dist(p2,p3),dist(p2,p4),dist(p3,p4)]
        ls.sort()
        if ls[0]==ls[1]==ls[2]==ls[3]:
            if ls[4]==ls[5]:
                return True
        return False
```
 