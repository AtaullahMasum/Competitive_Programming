class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_count = 0
        for key, value in freq.items():
            if max_count < value:
                max_count = value
        count = 0
        for key, value in freq.items():
            if max_count == value:
                count += value
        return count
        