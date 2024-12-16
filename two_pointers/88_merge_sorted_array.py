from typing import List

class Solution:
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # given that both arrays are in non-decreasing order, and last m elements of num1 array are 0-s, we need to override them with the largest numbers
        # to find the largest numbers among both lists, we can start comparing last elements of num2 and num1[:n] 
        # and overriding zeroes with the largest number while decrementing pointers
        # First two pointers solution:

        first = m - 1
        second = n - 1
        while first >= 0 and second >= 0:
            if nums1[first] < nums2[second]:
                nums1[first + second + 1] = nums2[second]
                second -= 1
            else:
                nums1[first + second + 1] = nums1[first]
                first -= 1
        while first >= 0:
            nums1[first + second + 1] = nums1[first]
            first -= 1
        while second >= 0:
            nums1[first + second + 1] = nums2[second]
            second -= 1

        # Second two pointers solution: get rid of 2 while loops as when second pointer exhausts, no need to copy the rest of the elements from the first array
        
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mth = m - 1
        nth = n - 1
        while nth >= 0:
            if mth >= 0 and nums1[mth] > nums2[nth]:
                nums1[mth + nth + 1] = nums1[mth]
                mth -= 1
            else:
                nums1[mth + nth + 1] = nums2[nth]
                nth -= 1

