class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = {}
        for i in range(len(nums)):
            #print(n_dict)
            if target - nums[i] in n_dict.values():
                return [i, nums.index(target - nums[i])]
            
            n_dict[i] = nums[i]
            
