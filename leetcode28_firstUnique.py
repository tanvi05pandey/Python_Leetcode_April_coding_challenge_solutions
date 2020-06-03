class FirstUnique:

    def __init__(self, nums):
        self.nums = nums
        self.d = {}
        self.q = []
        for item in nums:
            self.add(item)


    def showFirstUnique(self) -> int:
        while len(self.q) > 0 and self.d[self.q[0]] > 1:
            self.q.pop(0)
        if len(self.q) == 0:
            return -1
        else: return self.q[0]


    def add(self, value: int) -> None:
        if value in self.d:
            self.d[value] += 1
        else:
            self.d[value] = 1
            self.q.append(value)

firstUnique = FirstUnique([2,3,5]);
print(firstUnique.showFirstUnique())
firstUnique.add(5);
print(firstUnique.showFirstUnique())
firstUnique.add(2);
print(firstUnique.showFirstUnique())
firstUnique.add(3);
print(firstUnique.showFirstUnique())