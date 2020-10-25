class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        points, power = 0, P
        up, down = 0, len(tokens) - 1
        while up <= down and (points or power >= tokens[up]):
            if power >= tokens[up]:
                points += 1
                power -= tokens[up]
                up += 1
            elif up != down:
                points -= 1
                power += tokens[down]
                down -= 1
            else:
                break
        return points