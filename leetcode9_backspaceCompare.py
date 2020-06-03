#Given two strings S and T, return if they are equal when both are typed into empty text editors.
# '#' means a backspace character.

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".


# def backspaceCompare(S, T):
#     def build(S):
#         lst = list()
#         for x in S:
#             if x != '#':
#                 lst.append(x)
#             else:
#                 lst.pop()
#         return ''.join(lst)
#     return build(S) == build(T)

#-----2nd approach using string reversal----------
import itertools

def backspaceCompare(S, T):
    def F(S):
        skip = 0
        for x in reversed(S):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                print(x)
                yield x
    return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))



print(backspaceCompare('ab#c', 'ad#c'))