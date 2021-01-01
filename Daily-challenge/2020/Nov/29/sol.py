class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        
        idx = start
        q = [start]
        
        while q:
            
            node = q.pop(0)
            if arr[node] == 0:
                return True
            if arr[node] < 0:
                continue
                
            for i in [node + arr[node], node - arr[node]]:
                if 0 <= i < n:
                    q.append(i)
                    
            arr[node] = -arr[node]
            
        
            
            
        return False