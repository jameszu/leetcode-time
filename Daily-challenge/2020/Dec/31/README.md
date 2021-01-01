# Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10<br>

## Idea
Just do while loop and convert to decimal

## Code
```python
class Solution:
    def largestRectangleArea(self, height):
        n = len(height)


        left = [1] * n
        right = [1] * n
        max_rect = 0

        for i in range(0, n):
            j = i - 1
            while j >= 0:
                if height[j] >= height[i]:
                    left[i] += left[j]
                    j -= left[j]
                else: break

        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n:
                if height[j] >= height[i]:
                    right[i] += right[j]
                    j += right[j]
                else: break

        for i in range(0, n):
            max_rect = max(max_rect, height[i] * (left[i] + right[i] - 1))

        return max_rect
        
```