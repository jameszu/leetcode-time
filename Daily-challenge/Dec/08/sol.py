class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
       
        count = 0
        d = collections.defaultdict(int)

            
        for item in time:
            if item % 60 == 0:
                count += d[0]
            else:
                count += d[60-item%60]
            d[item%60] += 1
                
        return count