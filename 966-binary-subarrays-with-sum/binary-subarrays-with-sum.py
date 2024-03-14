class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        sum_count = {0: 1}  # Dictionary to keep track of the count of sums encountered
        cur_sum = 0  # Current sum

        for num in nums:
            cur_sum += num
            if cur_sum - goal in sum_count:
                count += sum_count[cur_sum - goal]
            if cur_sum in sum_count:
                sum_count[cur_sum] += 1
            else:
                sum_count[cur_sum] = 1

        return count