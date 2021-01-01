class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs = []
            for a, b in zip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) > 2:
                    return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:

            
        lena = len(A)
        lenb = len(B)
        if lena != lenb:
            return False
        elif sorted(A) != sorted(B):
            return False
        elif A==B and len(set(A))==len(A):
            return False
        else:
            count = 0
            for i in range(lena):
                if A[i] != B[i]:
                    count += 1
                    if count == 3:
                        return False
            return True