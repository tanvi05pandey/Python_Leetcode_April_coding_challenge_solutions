# Given a string containing only three types of characters: '(', ')' and '*', write a function
# to check whether this string is valid. We define the validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.

# Example 1:
# Input: "()"
# Output: True

def checkValidString(s):
    # balance of left parenthesis and right parenthesis
    leftBalance = rightBalance = 0
    n = len(s)
    for i in range(n):
        # if char is ( or * - we increment leftBalance value
        if s[i] in "(*":
            print("1st if")
            leftBalance += 1
        # else decrement it
        else:
            print("1st else")
            leftBalance -= 1
        # we check right balance value starting from the end (right side)
        if s[n-i-1] in "*)":
            print("2nd if")
            rightBalance += 1
        else:
            print("2nd else")
            rightBalance -= 1
        # if any balance goes negative we have the case where order of parenthesis is wrong
        # e.g. )(  -> leftBalance will be -1 and rightBalance will be -1 after first iteration
        # or ((( - leftBalance is OK, but rightBalance will be -1 after first iteration
        if leftBalance < 0  or rightBalance < 0:
            return False
    return True



print(checkValidString('**))'))
#print(checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
#
# print(checkValidString('()'))
#print(checkValidString("(*))"))

