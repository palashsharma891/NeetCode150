class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # can use hashing, or
        return len(set(nums)) != len(nums)
    
    # TC: O(n) SC: O(n) same for both approaches
    
