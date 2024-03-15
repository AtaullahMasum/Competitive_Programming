class Solution:
    def findAllPermutation(self, index, nums, result):
        if index == len(nums):
            result.append(nums[:])
            return 
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.findAllPermutation(index+1, nums, result)
            nums[i], nums[index] = nums[index], nums[i]
    def findallpermutation(self, freq, nums, result, each_result):
        if len(each_result)==len(nums):
            result.append(each_result[:])
            return
        for i in range(len(nums)):
            if not freq[i]:
                freq[i] = True
                each_result.append(nums[i])
                self.findallpermutation(freq, nums, result, each_result)
                each_result.pop()
                freq[i] = False
            

    def permute(self, nums: List[int]) -> List[List[int]]:
        #method 1
        result = []
        self.findAllPermutation(0, nums, result)
        return result
        #method 2
        n = len(nums)
        freq = [False]*n
        result , each_result = [], []
        self.findallpermutation(freq,nums, result, each_result)
        return result
        