class Solution:
    def findSubset(self, index, nums, result, each_result):
        result.append(each_result[:])
        for i in range(index, len(nums)):
            if i >   index and nums[i]==nums[i-1]:
                continue
            each_result.append(nums[i])
            self.findSubset(i+1, nums, result, each_result)
            each_result.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        each_result = []
        nums.sort()
        self.findSubset(0,nums, result, each_result)
        return result
        