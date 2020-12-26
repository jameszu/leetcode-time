# Diagonal Traverse

Solution
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.<br>

## Idea
Just do while loop and convert to decimal

## Code
```python
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        resp = []
        if not len(matrix): return resp
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, 0
        while len(resp) < m * n:
            # up-right
            while i >= 0 and j < n:
                resp.append(matrix[i][j])
                i -= 1
                j += 1
            if j < n:
                i += 1
            else:
                i += 2
                j -= 1

            # down-left
            while j >= 0 and i < m:
                resp.append(matrix[i][j])
                i += 1
                j -= 1
            if i < m:
                j += 1
            else:
                j += 2
                i -= 1
        
        return resp
        
```