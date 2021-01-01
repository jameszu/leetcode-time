# Reach a Number
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].<br>

## Idea
Just do while loop and convert to decimal

## Code
```python
class Solution:
    def reachNumber(self, target: int) -> int:
        bound = ceil(sqrt(2*abs(target)+0.25) - 0.5)
        if target % 2 == 0:
            if bound % 4 == 1: bound += 2
            if bound % 4 == 2: bound += 1
        else:
            if bound % 4 == 3: bound += 2
            if bound % 4 == 0: bound += 1
                
        return bound
        
```