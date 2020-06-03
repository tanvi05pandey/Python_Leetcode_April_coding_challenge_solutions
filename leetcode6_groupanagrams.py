#Given an array of strings, group anagrams together.
from collections import defaultdict


def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams(["",'b']))


total = 0
for abc in range(5):
    total = total + abc
print(total)