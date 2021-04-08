
# Space: O(1)
# Time: O(logn)

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if not nums1:
            length = len(nums2)
            if length % 2 == 0:
                return (nums2[length // 2] + nums2[length // 2 - 1]) / 2
            elif length % 2 != 0:
                return nums2[length // 2] / 1

        if not nums2:
            length = len(nums1)
            if length % 2 == 0:
                return (nums1[length // 2] + nums1[length // 2 - 1]) / 2
            elif length % 2 != 0:
                return nums1[length // 2] / 1

        length1, length2 = len(nums1), len(nums2)

        if length1 > length2: return self.findMedianSortedArrays(nums2, nums1)

        k = (length1 + length2) // 2

        left, right = 0, length1

        while left < right:
            m1 = (left + right) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            else:
                right = m1

        m1 = left
        m2 = k - m1

        c1 = max(nums1[m1 - 1] if m1 > 0 else -float('inf'), nums2[m2 - 1] if m2 > 0 else -float('inf'))
        c2 = min(nums1[m1] if m1 < length1 else float('inf'), nums2[m2] if m2 < length2 else float('inf'))

        return (c1 + c2) / 2 if (length1 + length2) % 2 == 0 else c1 / 1





