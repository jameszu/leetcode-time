class Solution:
    def reachNumber(self, target: int) -> int:
        bound = ceil(sqrt(2*abs(target)+0.25) - 0.5)
        if target % 2 == 0:
            if bound % 4 == 1: bound += 2
            if bound % 4 == 2: bound += 1
        else:
            if bound % 4 == 3: bound += 2
            if bound % 4 == 0: bound += 1
                
        return bound