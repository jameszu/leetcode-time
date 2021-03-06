#   Minimum Number of Arrows to Burst Balloons
There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.

Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Example 4:

Input: points = [[1,2]]
Output: 1
Example 5:

Input: points = [[2,3],[2,3]]
Output: 1
 

Constraints:

0 <= points.length <= 104
points.length == 2
-231 <= xstart < xend <= 231 - 1

## Idea
Another interesting question. <br>
Bascially finding overlaps in a list of ranges. We can think of a bunch of schedule bars in a diagram and fining the overlappes. <br>
We can just think the ending part. We sort the array by their ending for the sake of confirming the first bar. <br>
Then we just need a while loop to check if the value of cur_starting is less than the arr[i][0], the first value of the ith element. <br>
By doing so we make know two bar/element will not overlap so we add an arrow and replace the cur_start. <br>
Otherwise we just need simply skip the current i. 

---
Interesting it count as greedy algorithm<br>

## Code
```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        lenz = len(points)
        if lenz == 0:
            return 0
        
        points.sort(key=lambda key : key[1])
        starting = points[0][1]
        count = 1
        i = 0
        while i < lenz:
            

            if starting >= points[i][0]:
                i += 1
                continue
            count += 1
            starting = points[i][1]
            i += 1
        return count
            
```