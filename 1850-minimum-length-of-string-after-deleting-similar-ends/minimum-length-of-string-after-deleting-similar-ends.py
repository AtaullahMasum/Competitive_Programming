class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s [right]:
                while s[left] == s[right] and left < right:
                    left += 1
                right -= 1
                while s[right]==s[right+1] and right >= 0:
                    right -= 1
            else:
                break
        return len(s[left:right+1])
        