class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        left = 0
        right = len(tokens) - 1
        while left <= right:
            if power >= tokens[left] :
                power -= tokens[left]
                score += 1
                left += 1
            else:
                if power + tokens[right] > power and score != 0 and right != left:
                    power += tokens[right]
                    right -= 1
                    score -= 1
                else:
                    break
        return score

            
        