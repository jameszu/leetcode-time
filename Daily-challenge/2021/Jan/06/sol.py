class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo = 0
        hi = len(arr)
        
        while lo < hi:
            mid = (lo+hi)//2
            if arr[mid] - mid-1 < k:
                lo = mid +1
            else:
                hi = mid
        return lo+k
            