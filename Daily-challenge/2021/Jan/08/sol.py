class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        t1 = ""
        t2 = ""
        for i in word1:
            t1 += i
            
        for j in word2:
            t2 += j
            
        return t1 == t2