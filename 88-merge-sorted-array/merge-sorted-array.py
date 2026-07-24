class Solution(object):
    def merge(self, nums1, m, nums2, n):
        right = n+m-1
        while n>0:
            if m>0 and nums1[m-1] > nums2[n-1]:
                nums1[right] = nums1[m-1]
                m -= 1
            else:
                nums1[right]= nums2[n-1]
                n -= 1
            right -= 1
            

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        