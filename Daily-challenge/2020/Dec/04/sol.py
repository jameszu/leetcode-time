class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        lst = []
        
        for i in range(1, n+1):
            if n % i == 0:
                lst += [i]
        if len(lst) < k:
            return -1
        return lst[k-1]