class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1.sort()
        nums2.sort()
        prev = None
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i]==nums2[j] and prev != nums1[i]:
                result.append(nums1[i])
                prev = nums1[i]
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                i += 1
                j += 1
        return result


        