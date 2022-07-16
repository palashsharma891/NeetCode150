class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
        
    
    def remove(self, node):
        l = node.prev
        r = node.next
        l.next = r
        r.prev = l
        
    
    def insert(self, node):
        last = self.right.prev
        last.next = node
        node.next = self.right
        node.prev = last
        self.right.prev = node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) #remove from wherever it was in the linked list
            self.insert(self.cache[key]) #insert it into the right end(mru)
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #remove if already exists
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key]) #insert as mru
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(self.left.next) #not using lru here works
            # del self.cache[lru.key] #need to use variable here
            
            del self.cache[self.left.next.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
