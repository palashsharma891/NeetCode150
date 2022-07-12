class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l]: #we are in the left sorted portion
                if target > nums[mid] or target < nums[l]: #target is not in left subarray
                    l = mid + 1 #so go to right subarray
                else:
                    r = mid - 1
                    
            elif nums[mid] <= nums[r]: #right sorted portion
                if target < nums[mid] or target > nums[r]: #target is not in right subarray
                    r = mid - 1 #so check in left
                else:
                    l = mid + 1
                    
        return -1
