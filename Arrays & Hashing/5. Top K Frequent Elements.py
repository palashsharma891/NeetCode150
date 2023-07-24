class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = Counter(nums)
        freq_count = [[] for i in range(len(nums)+1)]

        for key in num_map:
            freq_count[num_map[key]] += [key]

        ans = []
        for key in range(len(freq_count)-1, -1, -1):
            if freq_count[key] != []:
                for n in freq_count[key]: 
                    ans += [n]
                    if len(ans) == k:
                        return ans
                        

        '''
        num_map = Counter(nums)
        freq_map = defaultdict(list)
        
        for key in num_map:
            freq_map[num_map[key]] += [key]
        
        ans = []
        keys = sorted(freq_map.keys(), reverse=True)
        
        for key in keys:
            ans += freq_map[key]
        
        return ans[:k]'''
