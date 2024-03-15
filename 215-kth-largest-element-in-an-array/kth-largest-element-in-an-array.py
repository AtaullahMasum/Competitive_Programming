import heapq
class Solution:
    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low
        for j in range(low, high):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i
    def quickSelect(self, nums, low, high, k):
        if low <= high:
            pivot_index = self.partition(nums, low, high)
            if pivot_index == k:
                return nums[pivot_index]
            elif pivot_index < k:
                return self.quickSelect( nums, pivot_index+1, high, k)
            else:
                return self.quickSelect( nums, low, pivot_index-1, k )
    

        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return self.quickSelect(nums, 0, len(nums)-1, len(nums)-k)
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[k-1]
        