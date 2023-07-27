class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_pro = [1 for n in nums]
        right_pro = [1 for n in nums]

        for i in range(1, len(nums)):
            left_pro[i] = nums[i-1] * left_pro[i-1]

        for i in range(len(nums)-2, -1, -1):
            right_pro[i] = nums[i+1] * right_pro[i+1]

        for i in range(len(right_pro)):
            right_pro[i] *= left_pro[i]

        return right_pro
