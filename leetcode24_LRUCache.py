from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False)
        else:
            self.cache.move_to_end(key)
        self.cache[key] = value


cache = LRUCache(2);
cache.put(2,1)
cache.put(2,2)
cache.get(2);
cache.put(1,1);
cache.put(4, 1);
cache.get(2);

# ["LRUCache","put","put","get","put","put","get"]
# print([[2],[2,1],[2,2],[2],[1,1],[4,1],[2]])