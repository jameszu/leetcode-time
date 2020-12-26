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