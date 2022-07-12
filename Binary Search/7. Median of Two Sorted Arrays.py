class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #find mid of both
        mid1 = len(nums1) // 2
        mid2 = len(nums2) // 2
        
        #avg mid1+mid2
        s = (nums1[mid1] + nums2[mid2]) / 2
        
        #find closest number to this sum // 2
        l, r = 0, len(nums1) + len(nums2) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if mid > len(nums):
                if nums2[mid-len(nums1)] 
                r = len(nums) - 1
                
            if mid < len(nums1) and num1[mid] == s:
                return nums[mid]
            elif mid < len(nums2) and nums2[mid] == s:
                return nums[mid]
