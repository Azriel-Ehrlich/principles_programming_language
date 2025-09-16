from tail_recursive import tail_recursive

# find LCM of two numbers recursion without tail
def lcm(a, b):
    def gcd(x, y):
        if y == 0:
            return x
        return gcd(y, x % y)
    return abs(a * b) // gcd(a, b)

# find LCM of two numbers recursion with tail
@tail_recursive
def lcm_tail(a, b, acc=1):
    def gcd(x, y):
        if y == 0:
            return x
        return gcd(y, x % y)
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
