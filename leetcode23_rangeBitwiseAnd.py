#Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

def rangeBitwiseAnd(m, n) -> int:
    shift = 0
    while m != n:
        m >>= 1
        n >>= 1
        shift += 1
    return m << shift

print(rangeBitwiseAnd(5,7))