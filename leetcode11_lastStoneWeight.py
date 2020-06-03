# We have a collection of stones, each stone has a positive integer weight.
#
# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights
# x and y with x <= y.  The result of this smash is:
#
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

#the below method is naive. A better approach is using heap. Follow the program written after this.
# def lastStoneWeight(stones):
#     s = sorted(stones)
#     if len(stones) == 1:
#         return stones[0]
#     for i in range(len(stones)):
#         s= sorted(s)
#         print(s)
#         sub = s[-1]-s[-2]
#         s.pop(-2)
#         s.pop(-1)
#         s.append(sub)
#         if len(s) == 1:
#             return s[0]

import heapq
def lastStoneWeight(stones):
    stones = [-val for val in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        x = heapq.heappop(stones)
        y = heapq.heappop(stones)
        heapq.heappush(stones,-abs(x-y))
    return -stones[0] if stones else 0

print(lastStoneWeight([2,7,4,1,8,1]))
#print(lastStoneWeight([1]))
