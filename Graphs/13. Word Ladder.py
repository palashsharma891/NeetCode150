class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        nei = collections.defaultdict(list)
        
        wordList.append(beginWord) #works without this because the patterns for beginWord will be created in the BFS
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                nei[pattern].append(word)
                
        visited = set(beginWord)
        q = collections.deque()
        q.append(beginWord)
        res = 1
        
        while q:
            qlen = len(q)
            for i in range(qlen):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:] #beginWord's patterns are created and matched here
                    for neighbor in nei[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                            
            res += 1
            
        return 0
