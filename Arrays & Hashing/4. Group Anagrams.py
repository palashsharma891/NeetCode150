class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()

        """
        d = {}
        for s in strs:
            temp = ''.join(sorted(s))
            if temp in d:
                d[temp] += [s]
            else:
                d[temp] = [s]

        ans = []
        for k in d:
            ans += [d[k]]

        return ans
        """
