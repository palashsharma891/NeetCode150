zclass Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        [2,7,11,15]; 9
         l---><---r
        '''
        l, r = 0, len(numbers)-1
        while l < r:
            if  numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

        """
        TC: O(n)
        SC: O(1)
        """
