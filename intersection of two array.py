class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        z = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                z.append(nums1[i])
                nums2.remove(nums1[i])
        return z
