
# def singleNumber(nums):
#     nums.sort()
#     for i in list(dict.fromkeys(nums)):
#         if nums.count(i) == 1:
#             print(i)
# print(singleNumber([4,1,2,1,2]))


from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
# for k, c in groupby(input()):
#     print([int(k), len(list(c))])