class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = nums1 + nums2
        total.sort()
        l, r = 0, len(total) - 1
        m = (l + r) // 2

        if len(total) % 2 == 0:
            median = (total[m] + total[m + 1]) / 2
            return median
        
        return total[m]