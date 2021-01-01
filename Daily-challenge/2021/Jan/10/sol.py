class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 1
        test = False
        test1 = False
        while i <= len(arr)-1 and arr[i] > arr[i-1]:
            i += 1
            test1 = True
            
        while i <= len(arr)-1 and arr[i] < arr[i-1]:
            i += 1
            test = True
        return i-1 == len(arr) -1 and test and test1
                