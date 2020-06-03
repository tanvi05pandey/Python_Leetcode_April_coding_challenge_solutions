# A happy number is a number defined by the following process: Starting with any positive integer, replace the
# number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in
# 1 are happy numbers.

# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

def isHappy(n):
    # total = 0
    # for digit_str in str(n):
    #     digit = int(digit_str)
    #     total += digit * digit
    #
    # if total == 1 or total == 7:
    #     return True
    # else:
    #     if total < 10 or total == 0:
    #         return False
    #     else:
    #         return isHappy(total)
    #------Below approach is using Floyd's cycle detection algorithm-------------
    def next_num(num):
        return sum(map(lambda x:int(x)**2, str(num)))
    slow, fast = n, next_num(n)
    while slow != fast and fast != 1:
        print("slow: ",slow)
        print("fast: ",fast)
        slow = next_num(slow)
        print("new slow: ",slow)
        fast = next_num(next_num(fast))
        print("new fast: ",fast)
    return fast == 1 or not slow == fast

print(isHappy(2))

