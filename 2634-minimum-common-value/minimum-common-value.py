class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums3 = set(nums2)
        for num in nums1:
            if num in nums3:
                return num
        return -1
        