class Solution(object):
    def flipAndInvertImage(self, A):
        result = []
        for row in A:
            result.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
        return result