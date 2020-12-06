# Can Place Flowers

Solution
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length<br>
## Idea
It is really intestring, it is not a good question. THere is a very very simple solution but u need to be really abstract
## Code
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        lenz = len(flowerbed)
        count = 0
        
        while i < lenz and count < n:
            if flowerbed[i] == 0:
                if i == lenz - 1: 
                    nex = 0 
                else: nex = flowerbed[i+1]
                if i == 0: 
                    prev = 0 
                else: 
                    prev = flowerbed[i-1]
                if nex == 0 and prev == 0:
                    flowerbed[i] = 1
                    count += 1
                    
            i += 1
        return count == n
```