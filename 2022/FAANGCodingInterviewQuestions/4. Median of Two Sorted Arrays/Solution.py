from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        added_list = nums1 + nums2
        added_list.sort()

        if len(added_list) == 1:
            median = added_list[0]

        elif len(added_list) % 2 == 0:
            n = int(len(added_list) / 2)
            m = int((len(added_list) / 2) - 1)
            median = (added_list[n] + added_list[m]) / 2

        else:
            n = (len(added_list) // 2)
            median = added_list[n]

        return median


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 2], [3, 4]))
