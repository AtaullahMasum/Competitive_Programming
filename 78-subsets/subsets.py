class Solution:
    def findSubset(self, index,nums, result, each_result):
        if index == len(nums):
            result.append(each_result.copy())
            return 
        each_result.append(nums[index])
        self.findSubset(index+1, nums, result, each_result)
        each_result.pop()
        self.findSubset(index+1, nums, result, each_result)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        index = 0
        result = []
        each_result = []
        self.findSubset(0, nums, result, each_result)
        return result

        